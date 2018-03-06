from __future__ import unicode_literals

from functools import wraps
import io
import logging
import os
import re
import requests

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.six.moves.urllib.parse import urljoin
from django.utils.termcolors import colorize


logger = logging.getLogger(__name__)

base_url = settings.FALLBACK_STORAGE_URL
skip_re = getattr(settings, 'FALLBACK_STORAGE_SKIP', None)


def download_before_call(method):
    @wraps(method)
    def _fn(self, name, *args, **kwargs):
        if skip_re and re.search(skip_re, name):
            return method(self, name, *args, **kwargs)

        local = os.path.join(settings.MEDIA_ROOT, name)
        if not os.path.exists(local):
            remote = urljoin(base_url, name)
            import traceback
            traceback.print_stack()
            logger.debug("Attempting download '%s' -> '%s'", remote, name)
            try:
                data = requests.get(remote, timeout=5)
            except Exception as exc:
                logger.exception("Error while downloading %s: %s", remote, exc)
            else:
                if data.status_code == 200:
                    dirname = os.path.dirname(local)
                    if not os.path.exists(dirname):
                        os.makedirs(os.path.dirname(local))
                    with io.open(local, 'wb') as f:
                        f.write(data.content)

        return method(self, name, *args, **kwargs)

    return _fn


class FallbackStorage(FileSystemStorage):
    open = download_before_call(FileSystemStorage.open)
    path = download_before_call(FileSystemStorage.path)
    exists = download_before_call(FileSystemStorage.exists)
    size = download_before_call(FileSystemStorage.size)
    url = download_before_call(FileSystemStorage.url)


class ColorizingFormatter(logging.Formatter):
    def format(self, record):
        if record.levelno in (40, 50):
            record.msg = colorize(record.msg, fg='red')
        else:
            record.msg = colorize(record.msg, fg='blue')
        return super().format(record)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'http_fallback_storage': {
            '()': ColorizingFormatter,
        },
    },
    'handlers': {
        'http_fallback_storage_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'http_fallback_storage',
        },
    },
    'loggers': {
        'http_fallback_storage': {
            'level': 'DEBUG',
            'handlers': ['http_fallback_storage_console'],
        },
    },
}

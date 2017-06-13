from __future__ import unicode_literals

from functools import wraps
import io
import os
import requests

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.six.moves.urllib.parse import urljoin
from django.utils.termcolors import colorize


def download_before_call(method):
    @wraps(method)
    def _fn(self, name, *args, **kwargs):
        local = os.path.join(settings.MEDIA_ROOT, name)
        if not os.path.exists(local):
            remote = urljoin(settings.FALLBACK_STORAGE_URL, name)
            print(colorize(
                "Attempting download '%s' -> '%s'" % (remote, name),
                fg='blue',
            ))
            try:
                data = requests.get(remote)
            except Exception as exc:
                print(colorize(exc, fg='red'))
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

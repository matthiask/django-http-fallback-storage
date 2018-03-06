============================
django-http-fallback-storage
============================

When the production site uploads folder gets really big you don't want to
rsync everything to your local machine just to fix a few bugs. Only download
what is needed, right?

That's what this storage class does.

Usage
=====

0. Make sure that you only use this if ``DEBUG = True``
1. Add the following settings::

    DEFAULT_FILE_STORAGE = 'http_fallback_storage.FallbackStorage'
    FALLBACK_STORAGE_URL = 'http://example.com/media/'

2. Optionally, configure logging so that it's easy to see why page loads
   would be slow when fetching media files. Either of the following
   snippets should be fine when added to your settings file::

    import http_fallback_storage
    LOGGING = http_fallback_storage.LOGGING

   or::

    # LOGGING has already been defined
    import http_fallback_storage
    LOGGING.update(http_fallback_storage.LOGGING)

3. Optionally, specify a regular expression for skipping file downloads,
   e.g. the following regex to never download movies::

    FALLBACK_STORAGE_SKIP = r'(\.mp4|\.mov)$'

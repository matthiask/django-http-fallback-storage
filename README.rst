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
1. Add ``DEFAULT_FILE_STORAGE = 'http_fallback_storage.FallbackStorage``
   and ``FALLBACK_STORAGE_URL = 'http://example.com/media/'`` to your
   Django settings

==========
Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

- Added timeouts to downloads.
- Added the ``FALLBACK_STORAGE_SKIP`` setting which allows specifying a
  regular expression which, if it matches the filename, skips the fallback.
  If set to ``FALLBACK_STORAGE_SKIP = r'^test$'``, this avoids problems
  introduced e.g. by `easy-thumbnails
  <https://github.com/SmileyChris/easy-thumbnails/blob/c4483dc44cb748749df420d9cd1f57fb4fac469b/easy_thumbnails/utils.py#L67>`_.


`1.3`_ (2017-07-27)
~~~~~~~~~~~~~~~~~~~

- Removed the cache again. It lead to strange errors with accessing
  closed files.
- Switched from print() statements to logging. If you want the old
  behavior you should use ``http_fallback_storage.LOGGING`` as your
  Django ``LOGGING`` configuration (or merge the logging configuration
  dicts).


`1.2`_ (2017-06-06)
~~~~~~~~~~~~~~~~~~~

- Cache answers a bit. This is especially useful with non-existing
  files.


`1.1`_ (2016-11-19)
~~~~~~~~~~~~~~~~~~~

- Only write response data to the disk if HTTP status code is 200.
- Only access response data if there actually was a response.
- Avoid ``u''`` prefixes on strings printed to the console.


`1.0`_ (2016-08-26)
~~~~~~~~~~~~~~~~~~~

- Initial release!

.. _1.0: https://github.com/matthiask/django-http-fallback-storage/commit/eaf1510905
.. _1.1: https://github.com/matthiask/django-http-fallback-storage/compare/1.0...1.1
.. _1.2: https://github.com/matthiask/django-http-fallback-storage/compare/1.1...1.2
.. _1.3: https://github.com/matthiask/django-http-fallback-storage/compare/1.2...1.3
.. _Next version: https://github.com/matthiask/django-http-fallback-storage/compare/1.3...master

==========
Change log
==========

`Next version`_
~~~~~~~~~~~~~~~

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
.. _Next version: https://github.com/matthiask/django-http-fallback-storage/compare/1.2...master

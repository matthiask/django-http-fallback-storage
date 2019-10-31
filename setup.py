#!/usr/bin/env python

from io import open
import os
from setuptools import setup


def read(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, encoding="utf-8") as handle:
        return handle.read()


setup(
    name="django-http-fallback-storage",
    version="1.6",
    description="",
    long_description=read("README.rst"),
    author="Matthias Kestenholz",
    author_email="mk@feinheit.ch",
    url="https://github.com/matthiask/django-http-fallback-storage/",
    license="BSD License",
    platforms=["OS Independent"],
    py_modules=["http_fallback_storage"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    install_requires=["requests"],
    zip_safe=False,
)

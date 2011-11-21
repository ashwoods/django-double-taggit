#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from setuptools import setup, find_packages


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__=='__main__':
    setup(
        name = 'django-taggit-tag-it',
        version = get_version(),
        license = 'Apache License version 2',
        long_description = read('README'),
        platforms=['any'],
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        packages = find_packages(),
        setup_requires = ["setuptools_git >= 0.3",],
        include_package_data = True,
        zip_safe = False,
    )


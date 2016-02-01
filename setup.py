# -*- coding: utf-8 -*-
#
# This file is part of DoJSON
# Copyright (C) 2015, 2016 CERN.
#
# DoJSON is free software; you can redistribute it and/or
# modify it under the terms of the Revised BSD License; see LICENSE
# file for more details.

"""DoJSON is a simple Pythonic JSON to JSON converter."""

import os
import re

from setuptools import setup


# Get the version string.  Cannot be done with import!
with open(os.path.join('dojson', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

tests_require = [
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.1.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
    'coverage>=4.0.0',
    'mock',
]

extras_require = {
    'docs': [
        'Sphinx>=1.3',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    extras_require['all'].extend(reqs)

setup(
    name='dojson',
    version=version,
    url='http://github.com/inveniosoftware/dojson/',
    license='BSD',
    author='Invenio collaboration',
    author_email='info@invenio-software.org',
    description=__doc__,
    long_description=open('README.rst').read(),
    packages=['dojson'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    setup_requires=[
        'pytest-runner>=2.6.2',
        'setuptools>=17.1',
    ],
    install_requires=[
        'click',
        'lxml',
        'six',
    ],
    extras_require=extras_require,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 1 - Planning',
    ],
    tests_require=tests_require,
    entry_points={
        'console_scripts': [
            'dojson = dojson.cli:cli',
        ],
        'dojson.contrib.marc21': [
            'bd00x = dojson.contrib.marc21.fields.bd00x',
            'bd01x09x = dojson.contrib.marc21.fields.bd01x09x',
            'bd1xx = dojson.contrib.marc21.fields.bd1xx',
            'bd20x24x = dojson.contrib.marc21.fields.bd20x24x',
            'bd25x28x = dojson.contrib.marc21.fields.bd25x28x',
            'bd3xx = dojson.contrib.marc21.fields.bd3xx',
            'bd4xx = dojson.contrib.marc21.fields.bd4xx',
            'bd5xx = dojson.contrib.marc21.fields.bd5xx',
            'bd6xx = dojson.contrib.marc21.fields.bd6xx',
            'bd70x75x = dojson.contrib.marc21.fields.bd70x75x',
            'bd76x78x = dojson.contrib.marc21.fields.bd76x78x',
            'bd80x83x = dojson.contrib.marc21.fields.bd80x83x',
            'bd84188x = dojson.contrib.marc21.fields.bd84188x',
        ],
        'dojson.contrib.to_marc21': [
            'bd00x = dojson.contrib.to_marc21.fields.bd00x',
            'bd01x09x = dojson.contrib.to_marc21.fields.bd01x09x',
            'bd1xx = dojson.contrib.to_marc21.fields.bd1xx',
            'bd20x24x = dojson.contrib.to_marc21.fields.bd20x24x',
            'bd25x28x = dojson.contrib.to_marc21.fields.bd25x28x',
            'bd3xx = dojson.contrib.to_marc21.fields.bd3xx',
            'bd4xx = dojson.contrib.to_marc21.fields.bd4xx',
            'bd5xx = dojson.contrib.to_marc21.fields.bd5xx',
            'bd6xx = dojson.contrib.to_marc21.fields.bd6xx',
            'bd70x75x = dojson.contrib.to_marc21.fields.bd70x75x',
            'bd76x78x = dojson.contrib.to_marc21.fields.bd76x78x',
            'bd80x83x = dojson.contrib.to_marc21.fields.bd80x83x',
            'bd84188x = dojson.contrib.to_marc21.fields.bd84188x',
        ],
        'dojson.contrib.marc21_authority': [
            'ad00x = dojson.contrib.marc21.fields.ad00x',
            'ad01x09x = dojson.contrib.marc21.fields.ad01x09x',
            'ad1xx3xx = dojson.contrib.marc21.fields.ad1xx3xx',
            'ad260360 = dojson.contrib.marc21.fields.ad260360',
            'ad4xx = dojson.contrib.marc21.fields.ad4xx',
            'ad5xx = dojson.contrib.marc21.fields.ad5xx',
            'ad64x = dojson.contrib.marc21.fields.ad64x',
            'ad663666 = dojson.contrib.marc21.fields.ad663666',
            'ad66768x = dojson.contrib.marc21.fields.ad66768x',
            'ad7xx = dojson.contrib.marc21.fields.ad7xx',
            'ad8xx = dojson.contrib.marc21.fields.ad8xx',
        ],
        'dojson.contrib.marc21_holdings': [
            'hd00x = dojson.contrib.marc21.fields.hd00x',
            'hd0xx = dojson.contrib.marc21.fields.hd0xx',
            'hd3xx5xx84x = dojson.contrib.marc21.fields.hd3xx5xx84x',
            'hd85xhd88x = dojson.contrib.marc21.fields.hd85xhd88x',
        ],
        'dojson.cli.rule': [
            'marc21 = dojson.contrib.marc21:marc21',
            'marc21_authority = dojson.contrib.marc21:marc21_authority',
            'marc21_holdings = dojson.contrib.marc21:marc21_holdings',
            'to_marc21 = dojson.contrib.to_marc21:to_marc21',
        ],
        'dojson.cli.load': [
            'json = dojson.utils:load',
            'marcxml = dojson.contrib.marc21.utils:load',
        ],
        'dojson.cli.dump': [
            'json = json:dumps',
            'marcxml = dojson.contrib.to_marc21.utils:dumps',
        ],
    }
)

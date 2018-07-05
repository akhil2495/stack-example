#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'aggiestack',
    version = '0.1',
    author = 'Akhil Babu Manam',
    author_email = 'manamakhilbabu@gmail.com',
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'aggiestack = aggiestack.cli:main'
        ]
    },
    )

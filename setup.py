#!/usr/bin/env python

from setuptools import setup, find_packages, Command
from aggiestack import __version__

setup(
    name = 'aggiestack',
    version = '0.1',
    author = 'Akhil Babu Manam',
    author_email = 'manamakhilbabu@gmail.com',
    packages = find_packages(),
    install_requires = ['docopt'],
    entry_points = {
        'console_scripts':[
            'aggiestack=aggiestack.cli:main'
        ],
    }, 
)

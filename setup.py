from setuptools import setup

setup(
    name = 'aggiestack',
    author = 'Akhil Babu Manam',
    install_requires = ['docopt'],
    entry_points = {
        'console_scripts': [
            'aggiestack=aggiestack.cli:main',
        ],
    },

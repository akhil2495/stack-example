from setuptools import setup

setup(
    name = 'aggiestack',
    version = '0.1'
    author = 'Akhil Babu Manam',
    install_requires = ['docopt'],
    entry_points = {
        'console_scripts': [
            'aggiestack=aggiestack.aggiestack:main',
        ],
    },

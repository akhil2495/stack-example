## Makefile (for controlling the interface)

PACKAGE=aggiestack

PYTHON=python2

all:

install:
	$(PYTHON) setup.py develop

"""
aggiestack

Usage:
  aggiestack config
  aggiestack show

Examples:
  aggiestack config
  aggiestack show

Help:
  Have only two types of commands aggiestack config or aggiestack show
"""

from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    import aggiestack.commands
    options = docopt(__doc__, version=VERSION)

    print options

    for (k,v) in options.items():
        if hasattr(aggiestack.commands, k) and v:
            module = getattr(aggiestack.commands, k)
            aggiestack.commands = getmembers(module, isclass)
            command = [command[1] for command in aggiestack.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
    print "hello"

def hello():
    return ("hello")

def say_hello():
    print hello()

main()

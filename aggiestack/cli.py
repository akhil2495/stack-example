"""
aggiestack

Usage:
  aggiestack config --hardware <input_file>
  aggiestack config --images <input_file>
  aggiestack config --flavors <input_file>
  aggiestack show hardware
  aggiestack show images
  aggiestack show flavors
  aggiestack show all

Examples:
  aggiestack config --hardware hdwr-config.txt
  aggiestack config --images image-config.txt
  aggiestack config --flavors flavor-config.txt
  aggiestack show hardware
  aggiestack show images
  aggiestack show flavors
  aggiestack show all
  

Help:
  Have only two types of commands aggiestack config or aggiestack show
"""

from commands.config import config_command
from commands.show import show_command
from docopt import docopt


def main():
    import aggiestack.commands
    options = docopt(__doc__, version='0.1')

    command_check = False
    # for config commands
    if options['config'] == True:
        if options['--hardware'] == True:
            if options['<input_file>']:
                config_command('hardware', options['<input_file>'])
                command_check = True

        elif options['--images'] == True:
            if options['<input_file>']:
                config_command('images', options['<input_file>'])
                command_check = True
 
        elif options['--flavors'] == True:
            if options['<input_file>']:
                config_command('flavors', options['<input_file>'])
                command_check = True

    # for show commands
    if options['show'] == True:
        if options['hardware'] == True:
            show_command('hardware')
            command_check = True

        elif options['images'] == True:
            show_command('images')
            command_check = True

        elif options['flavors'] == True:
            show_command('flavors')
            command_check = True
 
        elif options['all'] == True:
            show_command('all')
            command_checl = True

    # error message if not a recognized command
    if command_check == False:
        print 'Error : Wrong commands, use this format'
        print options

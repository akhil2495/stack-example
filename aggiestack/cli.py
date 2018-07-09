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
from commands.config import config_log
from commands.show import show_log
from docopt import docopt
import sys
import os

def executed_command():
    com = ""
    i = 0
    for word in sys.argv:
        if i == 0:
            word = 'aggiestack'
        com += word + " "
        i += 1
    com += ":: "
    return com

def main():
    import aggiestack.commands
    dirname = os.path.dirname(os.path.realpath(__file__))
    if sys.argv[1] is not 'show' or sys.argv[1] is not 'config':
        print 'ERROR : Wrong command arguments'
        if os.path.isfile('log-files/aggiestack-log.txt'):
            with open(os.path.join(dirname, 'log-files/aggiestack-log.txt'), 'a') as file_handle:
                file_handle.write(executed_command() + 'FAILURE')
        else:
            with open(os.path.join(dirname, 'log-files/aggiestack-log.txt'), 'w') as file_handle:
                file_handle.write(executed_command() + 'FAILURE')
    elif len(sys.argv) == 4:
        if sys.argv[2] not in arg2_list:
            print 'ERROR : Wrong command arguments'
            if os.path.isfile('log-files/aggiestack-log.txt'):
                with open(os.path.join(dirname, 'log-files/aggiestack-log.txt'), 'a') as file_handle:
                    file_handle.write(executed_command() + 'FAILURE')
            else:
                with open(os.path.join(dirname, 'log-files/aggiestack-log.txt'), 'w') as file_handle:
                    file_handle.write(executed_command() + 'FAILURE')

    options = docopt(__doc__, version='0.1')

    command_check = False
    # for config commands
    if options['config'] == True:
        if options['--hardware'] == True:
            if options['<input_file>']:
                config_command('hardware', options['<input_file>'], executed_command())
                command_check = True

        elif options['--images'] == True:
            if options['<input_file>']:
                config_command('images', options['<input_file>'], executed_command())
                command_check = True
 
        elif options['--flavors'] == True:
            if options['<input_file>']:
                config_command('flavors', options['<input_file>'], executed_command())
                command_check = True

    # for show commands
    if options['show'] == True:
        if options['hardware'] == True:
            show_command('hardware', executed_command())
            command_check = True

        elif options['images'] == True:
            show_command('images', executed_command())
            command_check = True

        elif options['flavors'] == True:
            show_command('flavors', executed_command())
            command_check = True
 
        elif options['all'] == True:
            show_command('all')
            command_check = True

    # error message if not a recognized command
    if command_check == False:
        print 'ERROR : Wrong commands, use this format'
        print options
    

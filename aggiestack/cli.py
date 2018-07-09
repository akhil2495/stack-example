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
  aggiestack admin show hardware
  aggiestack admin can_host <machine_name> <flavor>

Examples:
  aggiestack config --hardware hdwr-config.txt
  aggiestack config --images image-config.txt
  aggiestack config --flavors flavor-config.txt
  aggiestack show hardware
  aggiestack show images
  aggiestack show flavors
  aggiestack show all
  aggiestack admin show hardware
  aggiestack admin can_host <machine_name> <flavor>

Help:
  Have only two types of commands aggiestack config or aggiestack show
"""

from commands.config import config_command
from commands.show import show_command
from commands.config import config_log
from commands.show import show_log
from commands.admin import admin_show_command
from commands.admin import admin_log
from commands.admin import admin_can_host_command
from docopt import docopt
import sys
import os

def check_command():
    config_list = [
        'config --hardware ',
        'config --images ',
        'config --flavors '
    ]
    show_list = [
        'show hardware ',
        'show images ',
        'show flavors ',
        'show all '
    ]
    admin_list = [
        'admin show hardware ',
        'admin can_host '
    ]
    check = ''
    wrong_cmd_flag = False
    if sys.argv[1] == 'config':
        if len(sys.argv) != 4:
            wrong_cmd_flag = True
        for i in range(len(sys.argv) - 2):
            check += sys.argv[i+1] + " "
        if check not in config_list:
            wrong_cmd_flag = True

    elif sys.argv[1] == 'show':
        if len(sys.argv) != 3:
            wrong_cmd_flag = True
        for i in range(len(sys.argv) - 1):
            check += sys.argv[i+1] + " "
        if check not in show_list:
            wrong_cmd_flag = True

    elif sys.argv[1] == 'admin':
        if len(sys.argv) == 4:
            for i in range(len(sys.argv) - 1):
                check += sys.argv[i+1] + " "
            if check not in admin_list:
                wrong_cmd_flag = True
        elif len(sys.argv) == 5:
            for i in range(len(sys.argv) - 3):
                check += sys.argv[i+1] + " "
            if check not in admin_list:
                wrong_cmd_flag = True
        else:
            wrong_cmd_flag = True
    return wrong_cmd_flag

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

    # checking if commands are good
    dirname = os.path.dirname(os.path.realpath(__file__))
    if check_command():
        print 'ERROR : Wrong commands, use this format'
        if os.path.isfile('log-files/aggiestack-log.txt'):
            with open(os.path.join(dirname, 'log-files/aggiestack-log.txt'), 'a') as file_handle:
                file_handle.write(executed_command() + 'FAILURE\n')
        else:
            with open(os.path.join(dirname, 'log-files/aggiestack-log.txt'), 'w') as file_handle:
                file_handle.write(executed_command() + 'FAILURE\n')

    options = docopt(__doc__, version='0.1')

    # for config commands
    if sys.argv[1] == 'config':
        if options['config'] == True:
            if options['--hardware'] == True:
                if options['<input_file>']:
                    config_command('hardware', options['<input_file>'], executed_command())
            elif options['--images'] == True:
                if options['<input_file>']:
                    config_command('images', options['<input_file>'], executed_command())
            elif options['--flavors'] == True:
                if options['<input_file>']:
                    config_command('flavors', options['<input_file>'], executed_command())

    # for show commands
    if sys.argv[1] == 'show':
        if options['show'] == True:
            if options['hardware'] == True:
                show_command('hardware', executed_command())
            elif options['images'] == True:
                show_command('images', executed_command())
            elif options['flavors'] == True:
                show_command('flavors', executed_command())
            elif options['all'] == True:
                show_command('all',  executed_command())

    # for admin commands
    if sys.argv[1] == 'admin':
        if options['admin'] == True:
            if options['show'] == True:
                if options['hardware'] == True:
                    admin_show_command(executed_command())

            elif options['can_host'] == True:
                if options['<machine_name>']:
                    if options['<flavor>']:
                        admin_can_host_command(options['<machine_name>'], options['<flavor>'], executed_command())

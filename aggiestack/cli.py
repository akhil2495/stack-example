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
  aggiestack admin show instances
  aggiestack admin evacuate <rack_name>
  aggiestack admin remove <server_name>
  aggiestack admin add --mem <nmem> --disk <ndisk> --vcpus <nvcpu> --ip <ip> --rack <rack_name> <server_name>
  aggiestack server create --image <image_name> --flavor <flavor_name> <instance_name>
  aggiestack server delete <instance_name>
  aggiestack server list

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
  aggiestack admin show instances
  aggiestack admin evacuate <rack_name>
  aggiestack admin remove <server_name>
  aggiestack admin add --mem <nmem> --disk <ndisk> --vcpus <nvcpu> --ip <ip> --rack <rack_name> <server_name>
  aggiestack server create --image <image_name> --flavor <flavor_name> <instance_name>
  aggiestack server delete <instance_name>
  aggiestack server list

Help:
  Have only two types of commands aggiestack config or aggiestack show
"""

from commands.config import config_command
from commands.show import show_command
from commands.helpers import log
from commands.admin import admin_show_command
from commands.admin import admin_can_host_command
from commands.admin import admin_show_instances_command
from commands.server import server_create_command
from commands.server import server_delete_command
from commands.server import server_list_command
from commands.admin import admin_evacuate_command
from commands.admin import admin_remove_command
from commands.admin import admin_add_command
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
        'admin can_host ',
        'admin show instances ',
        'admin evacuate ',
        'admin remove ',
        'admin add --mem '
    ]
    server_list = [
        'server create --image ',
        'server delete ',
        'server list '
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
            if sys.argv[2] == 'evacuate' or sys.argv[2] == 'remove':
                for i in range(len(sys.argv) - 2):
                    check += sys.argv[i+1] + " "
            else:
                for i in range(len(sys.argv) - 1):
                    check += sys.argv[i+1] + " "
            if check not in admin_list:
                print check
                wrong_cmd_flag = True
        elif len(sys.argv) == 5:
            for i in range(len(sys.argv) - 3):
                check += sys.argv[i+1] + " "
            if check not in admin_list:
                wrong_cmd_flag = True
        elif len(sys.argv) == 14:
            for i in range(3):
                check += sys.argv[i+1] + " "
            if sys.argv[3] != '--mem' or sys.argv[5] != '--disk' or sys.argv[7] != '--vcpus' or sys.argv[9] != '--ip' or sys.argv[11] != '--rack':
                wrong_cmd_flag = True
            if check not in admin_list:
                wrong_cmd_flag = True
        else:
            wrong_cmd_flag = True
 
    elif sys.argv[1] == 'server':
        if len(sys.argv) == 8:
            check = ''
            for i in range(3):
                check += sys.argv[i+1] + ' '
            if check not in server_list:
                wrong_cmd_flag = True
            if sys.argv[5] != '--flavor':
                wrong_cmd_flag = True
        elif len(sys.argv == 4):
            check = ''
            for i in range(2):
                check += sys.argv[i+1] + ' '
            if check not in server_list:
                wrong_cmd_flag = True
        elif len(sys.argv == 3):
            check = ''
            for i in range(2):
                check += sys.argv[i+1] + ' '
            if check not in server_list:
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
        if os.path.isfile(os.path.join(dirname, 'aggiestack-log.txt')):
            with open(os.path.join(dirname, 'aggiestack-log.txt'), 'a') as file_handle:
                file_handle.write(executed_command() + 'FAILURE\n')
        else:
            with open(os.path.join(dirname, 'aggiestack-log.txt'), 'w') as file_handle:
                file_handle.write(executed_command() + 'FAILURE\n')
        options = docopt(__doc__, version='0.1')
        return

    options = docopt(__doc__, version='0.1')

    # for config commands
    if sys.argv[1] == 'config':
        if options['config'] == True:
            if options['--hardware'] == True:
                if options['<input_file>']:
                    config_command('hardware', 
                                   options['<input_file>'], 
                                   executed_command())
            elif options['--images'] == True:
                if options['<input_file>']:
                    config_command('images', 
                                   options['<input_file>'], 
                                   executed_command())
            elif options['--flavors'] == True:
                if options['<input_file>']:
                    config_command('flavors', 
                                   options['<input_file>'], 
                                   executed_command())

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
                elif options['instances'] == True:
                    admin_show_instances_command(executed_command())

            elif options['can_host'] == True:
                if options['<machine_name>']:
                    if options['<flavor>']:
                        admin_can_host_command(options['<machine_name>'], 
                                               options['<flavor>'], 
                                               executed_command())

            elif options['evacuate'] == True:
                if options['<rack_name>']:
                    admin_evacuate_command(options['<rack_name>'], 
                                           executed_command())

            elif options['remove'] == True:
                if options['<server_name>']:
                    admin_remove_command(options['<server_name>'], 
                                         executed_command())
   
            elif options['add'] == True:
                if options['<nmem>']:
                    if options['<ndisk>']:
                        if options['<nvcpu>']:
                            if options['<ip>']:
                                if options['<rack_name>']:
                                    if options['<server_name>']:
                                        admin_add_command(options['<nmem>'], 
                                                          options['<ndisk>'], 
                                                          options['<nvcpu>'], 
                                                          options['<ip>'], 
                                                          options['<rack_name>'], 
                                                          options['<server_name>'],
                                                          executed_command())

    # for server commands
    if sys.argv[1] == 'server':
        if options['server'] == True:
            if options['create'] == True:
                if options['--image'] == True:
                    if options['<image_name>']:
                        if options['--flavor'] == True:
                            if options['<flavor_name>']:
                                if options['<instance_name>']:
                                    server_create_command(options['<image_name>'], 
                                                          options['<flavor_name>'], 
                                                          options['<instance_name>'], 
                                                          executed_command())

            elif options['delete'] == True:
                if options['<instance_name>']:
                    server_delete_command(options['<instance_name>'], 
                                          executed_command())

            elif options['list'] == True:
                server_list_command(executed_command())

if __name__ == '__main__':
    main()

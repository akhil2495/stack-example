import os
from helpers import parse_flavors
from helpers import parse_hardware
from helpers import log

def admin_show_command(arg = ''):
    # arg : executed command

    directory = os.path.dirname(os.path.realpath(__file__)) 
    path = os.path.join(directory, '../server-config.txt')
    if os.path.isfile(path):
        with open(path) as file_handle:
            print file_handle.read()
        log(arg, 'SUCCESS\n')
    else:
        print 'ERROR : Hardware information not yet configured'
        log(arg, 'FAILURE\n')

def admin_can_host_command(arg1, arg2, arg3 = ''):
    # arg1 : name of the hardware
    # arg2 : name of the flavor
    # arg3 : executed command

    flavors = parse_flavors()
    hardware = parse_hardware('current')

    if arg2 not in flavors.keys():
        if arg3:
            print 'ERROR : Wrong flavor name'
        log(arg3, 'FAILURE\n')
        return False
    if arg1 not in hardware.keys():
        if arg3:
            print 'ERROR : Wrong hardware name'
        log(arg3, 'FAILURE\n')
        return False

    # checking if the machine name is in the hardware file and if the flavor can fit
    if flavors[arg2]['mem'] > hardware[arg1]['mem']:
        if arg3:
            print 'ERROR : Memory insufficient'
        log(arg3, 'FAILURE\n')
        return False
    elif flavors[arg2]['ndisks'] > hardware[arg1]['ndisks']:
        if arg3:
            print 'ERROR : Not sufficient disks'
        log(arg3, 'FAILURE\n')
        return False
    elif flavors[arg2]['vcpus'] > hardware[arg1]['vcpus']:
        if arg3:
            print 'ERROR : Not sufficient cpus'
        log(arg3, 'FAILURE\n')
        return False
    else:
        if arg3:
            print 'yes'
        log(arg3, 'SUCCESS\n')
        return True

def admin_show_instances(arg = ''):
    # arg : executed command

    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    instances = parse_instances()
    if instances:
        with open(path) as file_handle:
            print file_handle.read()
    else:
        print 'INFO : No instances running currently'
    log(arg, 'SUCCESS\n')

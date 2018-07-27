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
        ERR_MSG = 'ERROR : Hardware information not yet configured'
        log(arg, 'FAILURE\n', ERR_MSG)

def admin_can_host_command(arg1, arg2, arg3 = ''):
    # arg1 : name of the hardware
    # arg2 : name of the flavor
    # arg3 : executed command

    flavors = parse_flavors()
    hardware = parse_hardware('current')

    if arg2 not in flavors.keys():
        ERR_MSG = 'ERROR : Wrong flavor name'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    if arg1 not in hardware.keys():
        ERR_MSG = 'ERROR : Wrong hardware name'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False

    # checking if the machine name is in the hardware file and if the flavor can fit
    if flavors[arg2]['mem'] > hardware[arg1]['mem']:
        ERR_MSG = 'ERROR : Memory insufficient'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    elif flavors[arg2]['ndisks'] > hardware[arg1]['ndisks']:
        ERR_MSG = 'ERROR : Not sufficient disks'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    elif flavors[arg2]['vcpus'] > hardware[arg1]['vcpus']:
        ERR_MSG = 'ERROR : Not sufficient cpus'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    else:
        MSG = 'yes'
        log(arg3, 'SUCCESS\n', MSG)
        return True

def admin_show_instances(arg = ''):
    # arg : executed command

    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    instances = parse_instances()
    if instances:
        with open(path) as file_handle:
            print file_handle.read()
        log(arg, 'SUCCESS\n')
    else:
        INFO_MSG = 'INFO : No instances running currently'
        log(arg, 'SUCCESS\n', INFO_MSG)

def admin_evacuate(arg1, arg2):
    # arg1 : The rack name
    # arg2 : executed command

    # change the server configuration file
    deleted_servers = []
    hardware = parse_hardware('current')
    hardware['rack'].pop(arg1)
    for key in hardware['server'].keys():
        if hardware['server'][key]['rack'] == arg1:
            deleted_servers.append(key)
            hardware['server'].pop(key)
    update_hardware(hardware['server'], hardware['rack'])

    # store all instances on this rack
    instances = parse_instances('instance2imageflavor')

    # instances running in the rack from instance configuration file
    # add each instance one-by-one by checking
    for key in instances.keys():
        if instances[key]['server'] in deleted_servers:
            image = instances[key]['image']
            flavor = instances[key]['flavor']
            instances.pop(key)
            if create_server_command(image, flavor, key):
                continue
            else:
                if arg2:
                    print 'ERROR : ' + key + ' cannot be accommodated right now'

    # if something fails give an error/warning/info
    # update log
    log(arg2, 'SUCCESS\n')

#def admin_remove(arg1, arg2):
    # arg1 : The server name
    # arg2 : executed command

    #directory = os.path.dirname(os.path.realpath(__file__))
    #path = os.path.join(directory, '../') 

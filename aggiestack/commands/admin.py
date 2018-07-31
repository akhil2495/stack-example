import os
from helpers import parse_flavors
from helpers import parse_hardware
from helpers import log
from helpers import parse_instances
from helpers import update_hardware
from server import server_create_command
from helpers import update_instances

def admin_show_command(arg = ''):
    # arg : executed command
    # this is a common command and needs to be changed from common.py as well

    directory = os.path.dirname(os.path.realpath(__file__)) 
    path = os.path.join(directory, '../server-config.txt')
    if os.path.isfile(path):
        with open(path) as file_handle:
            print file_handle.read()
        log(arg, 'SUCCESS\n', '')
    else:
        ERR_MSG = 'ERROR : Hardware information not yet configured'
        log(arg, 'FAILURE\n', ERR_MSG)

def admin_can_host_command(arg1, arg2, arg3 = ''):
    # arg1 : name of the hardware
    # arg2 : name of the flavor
    # arg3 : executed command

    flavors = parse_flavors()
    hardware = parse_hardware('current')
    hardware = hardware['server']

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

def admin_show_instances_command(arg = ''):
    # arg : executed command

    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    instances = parse_instances()
    if instances:
        with open(path) as file_handle:
            print file_handle.read()
        log(arg, 'SUCCESS\n', '')
    else:
        INFO_MSG = 'INFO : No instances running currently'
        log(arg, 'SUCCESS\n', INFO_MSG)

def admin_evacuate_command(arg1, arg2):
    # arg1 : The rack name
    # arg2 : executed command

    # change the server configuration file
    deleted_servers = []
    hardware = parse_hardware('current')
    if hardware['rack'].has_key(arg1):
        hardware['rack'].pop(arg1)
    else:
        ERR_MSG = "ERROR: " + arg1 + " is not a rack"
        log(arg2, "FAILURE\n", ERR_MSG)
        return
    for key in hardware['server'].keys():
        if hardware['server'][key]['rack'] == arg1:
            deleted_servers.append(key)
            hardware['server'].pop(key)
    update_hardware(hardware['server'], hardware['rack'])

    # store all instances on this rack
    instances = parse_instances()

    # instances running in the rack from instance configuration file
    # add each instance one-by-one by checking
    for key in instances.keys():
        if instances[key]['server'] in deleted_servers:
            image = instances[key]['image']
            flavor = instances[key]['flavor']
            instances.pop(key)
            updated = update_instances(instances)
            if server_create_command(image, flavor, key):
                continue
            else:
                if arg2:
                    # can also store them into a file that can be run after a while
                    print 'ERROR: ' + key + ' cannot be accommodated right now'

    # if something fails give an error/warning/info
    # update log
    log(arg2, 'SUCCESS\n', '')

def admin_remove_command(arg1, arg2):
    # arg1 : The server name
    # arg2 : executed command

    # change server configuration file
    hardware = parse_hardware('current')
    if hardware['server'].has_key(arg1):
        hardware['server'].pop(arg1)
    else:
        ERR_MSG = "ERROR: " + arg1 + " is not a server"
        log(arg2, "FAILURE\n", ERR_MSG)
        return
    update_hardware(hardware['server'], hardware['rack'])
    
    # store all instances on this machine
    instances = parse_instances()
    print instances

    # add each instance one-by-one by checking
    for key in instances.keys():
        if instances[key]['server'] == arg1:
            image = instances[key]['image']
            flavor = instances[key]['flavor']
            instances.pop(key)
            updated = update_instances(instances)
            if server_create_command(image, flavor, key, ''):
                continue
            else:
                if arg2:
                    # can also store them into a file which can run later
                    print 'ERROR: ' + key + ' cannot be accommoated right now'

    # if something fails give an error/warning/info
    # update log
    log(arg2, 'SUCCESS\n', '')

def admin_add_command(arg1, arg2, arg3, arg4, arg5, arg6, arg7):
    # arg1 : memory
    # arg2 : num of disks
    # arg3 : num of virtual cpus
    # arg4 : ip
    # arg5 : rack name
    # arg6 : server name
    # arg7 : executed command

    # change server configuration file
    hardware = parse_hardware('current')
    racks = []
    for key in hardware['rack']:
        racks.append(key)
    ips = []
    for key in hardware['server']:
        ips.append(hardware['server'][key]['ip'])
    if arg5 not in racks:
        if arg4 not in ips:
            temp = dict()
            temp['mem'] = int(arg1)
            temp['ndisks'] = int(arg2)
            temp['vcpus'] = int(arg3)
            temp['ip'] = arg4
            temp['rack'] = arg5
        else:
            ERR_MSG = 'ERROR: The ip is already being used'
            log(arg7, 'FAILURE\n', ERR_MSG)
    else:
        ERR_MSG = 'ERROR: The rack specified is under maintenance or does not exist'
        log(arg7, 'FAILURE\n', ERR_MSG)
    hardware['server'][arg6] = temp
    update_hardware(hardware['server'], hardware['rack'])
    
    # update log
    log(arg7, 'SUCCESS\n', '')

def admin_show_imagecaches_command(arg1, arg2):
    # arg1 : rack name
    # arg2 : executed command

    hardware = parse_hardware('current')
    im2rack = parse_image_rack()
    images = parse_images()
    
    if arg1 in hardware['rack'].keys():
        rack2im = dict()
        for key, val in im2rack.items():
            for v in val:
                if rack2im.has_key(v):
                    rack2im[v].append(key)
                else:
                    rack2im[v] = []
                    rack2im.append(key)

        print 'List of images in ' + arg1 + ':'
        for image in rack2im[arg1]:
            print image
        print 'Space left in storage is ' + str(hardware['rack'][arg1]) + 'MB'
        log(arg2, 'SUCCESS\n', '')
    else:
        ERR_MSG = 'ERROR: Wrong server name specified'
        log(arg2, 'FAILURE\n', ERR_MSG)

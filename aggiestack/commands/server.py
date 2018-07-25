# command server

# help documentation
# commands possible :
# aggiestack server create --image IMAGE --flavor FLAVOR_NAME INSTANCE_NAME ---> creates instance INSTANCE_NAME, boots from IMAGE, configured as FLAVOR_NAME

# aggiestack server delete INSTANCE_NAME ---> delete the instance INSTANCE_NAME

# aggiestack server list ---> list all running servers (name, image and flavor)

import os
from shutil import copyfile
from admin import parse_hardware
from admin import parse_flavors
from admin import can_host
from helpers import log
from helpers import parse_images
from helpers import parse_instances
from helpers import update_instances

def server_create_command(arg1, arg2, arg3, arg4 = ''):
    # arg1 => IMAGE_NAME
    # arg2 => FLAVOR_NAME
    # arg3 => INSTANCE_NAME
    # arg4 => executed command

    directory = os.path.dirname(os.path.realpath(__file__)) 
    src_path = os.path.join(os.getcwd(), arg2)
    
    images = parse_images()
    flavors = parse_flavors()
    instances = parse_instances()
    if arg1 in images:
        if agr2 in flavors:
            instances[arg3] = {'image': arg1, 'flavor': arg2}
            # search for a server (verify if it can_host) 
            updated = update_instances(instances)
            log(arg4, 'SUCCESS\n')
        else:
            log(arg4, 'FAILURE\n')
            print 'ERROR: specified wrong flavor name'
    else:
        log(arg4, 'FAILURE\n')
        print 'ERROR: specified wrong image name'

def server_delete_command(arg1, arg2 = ''):
    # arg1 => INSTANCE_NAME
    # arg2 => executed command
    
    # delete instance
    instances = parse_instances()
    if instances.has_key(arg1):
        instances.pop(arg1, None)
        updated = update_instances(instances)
        log(arg2, 'SUCCESS\n')
    else:
        log(arg2, 'FAILURE\n')
        print 'ERROR: specified instance name does not exist'

def server_list_command(arg1 = ''):
    # arg1 => executed command

    instaces = parse_instances()
    for key in instances.keys():
        print key + ' ' + instances[key]['image'] + ' ' + instances[key]['flavor']
    log(arg1, 'SUCCESS\n')

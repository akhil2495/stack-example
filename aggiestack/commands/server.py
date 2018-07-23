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

def server_log(arg):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../aggiestack-log.txt')
    if os.path.isfile(path):
        with open(path, 'a') as file_handle:
            file_handle.write(arg)
    else:
        with open(path, 'w') as file_handle:
            file_handle.write(arg)

def parse_images():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../image-config.txt')
    image = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            for line in file_handle:
                if i > 0:
                    line = line.rstrip()
                    words = line.split()
                    image[words[0]] = {'image_name': words[0], 'image_path': words[1]}
                i += 1
    return image

def parse_instances():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    instance = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            temp = dict()
            for line in file_handle:
                if i > 0:
                    line = line.rstrip()
                    words = line.split()
                    temp['image'] = words[1]
                    temp['flavor'] = words[2]
                    instance[words[0]] = temp
     return instance

def update_instances(instances):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    
    if os.path.isfile(path):
        with open(path, 'w') as file_handle:
            f.write(str(len(instances.keys())))
            for key in instances.keys()
                f.write(key + ' ' + instances[key]['image'] + ' ' + instances[key]['flavor'])
    return True

def server_create_command(arg1, arg2, arg3, arg4):
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
            updated = update_instances(instances)
            server_log(arg4 + 'SUCCESS\n')
        else:
            server_log(arg4 + 'FAILURE\n')
            print 'ERROR: specified wrong flavor name'
    else:
        server_log(arg4 + 'FAILURE\n')
        print 'ERROR: specified wrong image name'

def server_delete_command(arg1, arg2):
    # arg1 => INSTANCE_NAME
    # arg2 => executed command
    
    # delete instance
    instances = parse_instances()
    if instances.has_key(arg1):
        instances.pop(arg1, None)
        updated = update_instances(instances)
        server_log(arg2 + 'SUCCESS\n')
    else:
        server_log(arg2 + 'FAILURE\n')
        print 'ERROR: specified instance name does not exist'

def server_list_command(arg1):
    # arg1 => executed command

    instaces = parse_instances()
    for key in instances.keys():
        print key + ' ' + instances[key]['image'] + ' ' + instances[key]['flavor']
    server_log(arg1 + 'SUCCESS\n')


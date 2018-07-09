# command config

# help documentation
# commands possible :
# aggiestack config --hardware file.txt ---> prints the h/w info available on cloud
# aggiestack config --images file.txt ---> prints the images available for the user to choose when creating virtual machines
# aggiestack config --flavors file.txt ---> prints the list of available flavors for the user when creating virtual machines

import os
from shutil import copyfile

def config_log(arg):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../log-files/aggiestack-log.txt')
    if os.path.isfile(path):
        with open(path, 'a') as file_handle:
            file_handle.write(arg)
    else:
        with open(path, 'w') as file_handle:
            file_handle.write(arg)

def config_command(arg1, arg2, arg3):
    # arg1 : hardware , images , flavors
    # arg2 : filename
    # arg3 : executed command

    directory = os.path.dirname(os.path.realpath(__file__)) 
    src_path = os.path.join(directory, '../' + arg2)
    
    if arg1 == 'hardware':
        # check if the file is in right format
        if os.path.isfile(src_path):
            dest_path = os.path.join(directory, '../config-files/hdwr-config.txt')
            if src_path != dest_path:
                copyfile(src_path, dest_path)
            config_log(arg3 + 'SUCCESS\n')
        else:
            print "ERROR : Specified file does not exist"
            config_log(arg3 + 'FAILURE\n')

    elif arg1 == 'images':
        # check if command is successful or not
        if os.path.isfile(src_path):
            dest_path = os.path.join(directory, '../config-files/image-config.txt')
            if src_path != dest_path:
                copyfile(src_path, dest_path)
            config_log(arg3 + 'SUCCESS\n')
        else:
            print "ERROR : Specified file does not exist"
            config_log(arg3 + 'FAILURE\n')

    elif arg1 == 'flavors':
        # check if command is successful or not
        if os.path.isfile(src_path):
            dest_path = os.path.join(directory, '../config-files/flavor-config.txt')
            if src_path != dest_path:
                copyfile(src_path, dest_path)
            config_log(arg3 + 'SUCCESS\n')
        else:
            print "ERROR : Specified file does not exist" 
            config_log(arg3 + 'FAILURE\n')

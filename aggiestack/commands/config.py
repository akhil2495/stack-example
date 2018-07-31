import os
from shutil import copyfile
from helpers import log

def config_command(arg1, arg2, arg3 = ''):
    # arg1 : hardware , images , flavors
    # arg2 : filename
    # arg3 : executed command

    directory = os.path.dirname(os.path.realpath(__file__)) 
    src_path = os.path.join(os.getcwd(), arg2)
    
    if arg1 == 'hardware':
        # check if the file is in right format
        if os.path.isfile(src_path):
            dest_path = os.path.join(directory, '../hdwr-config.txt')
            if os.path.normpath(src_path) != os.path.normpath(dest_path):
                copyfile(src_path, dest_path)
            dest_path = os.path.join(directory, '../server-config.txt')
            copyfile(src_path, dest_path)
            log(arg3, 'SUCCESS\n', '')
        else:
            ERR_MSG = "ERROR : Specified file does not exist"
            log(arg3, 'FAILURE\n', ERR_MSG)

    elif arg1 == 'images':
        # check if command is successful or not
        if os.path.isfile(src_path):
            dest_path = os.path.join(directory, '../image-config.txt')
            if os.path.normpath(src_path) != os.path.normpath(dest_path):
                copyfile(src_path, dest_path)
            log(arg3, 'SUCCESS\n', '')
        else:
            ERR_MSG = "ERROR : Specified file does not exist"
            log(arg3, 'FAILURE\n', ERR_MSG)

    elif arg1 == 'flavors':
        # check if command is successful or not
        if os.path.isfile(src_path):
            dest_path = os.path.join(directory, '../flavor-config.txt')
            if os.path.normpath(src_path) != os.path.normpath(dest_path):
                copyfile(src_path, dest_path)
            log(arg3, 'SUCCESS\n', '')
        else:
            ERR_MSG = "ERROR : Specified file does not exist" 
            log(arg3, 'FAILURE\n', ERR_MSG)

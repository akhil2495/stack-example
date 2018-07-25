import os
from helpers import log

def show_command(arg1, arg2 = ''):
    # arg1 : hardware , images , flavors
    # arg2 : executed command

    directory = os.path.dirname(os.path.realpath(__file__)) 
    #print os.getcwd()
    if arg1 == 'hardware':
        path = os.path.join(directory, '../hdwr-config.txt') 
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
            log(arg2, 'SUCCESS\n')
        else:
            print 'ERROR : Hardware information not yet configured'
            log(arg2, 'FAILURE\n')

    elif arg1 == 'images':
        path = os.path.join(directory, '../image-config.txt')
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
            log(arg2, 'SUCCESS\n')
        else:
            print 'ERROR : Image information not yet configured'
            log(arg2, 'FAILURE\n')
            
    elif arg1 == 'flavors':
        path = os.path.join(directory, '../flavor-config.txt')
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
            log(arg2, 'SUCCESS\n')
        else:
            print 'ERROR : Flavors information not yet configured'
            log(arg2, 'FAILURE\n')

    elif arg1 == 'all':
        path1 = os.path.join(directory, '../hdwr-config.txt')
        path2 = os.path.join(directory, '../image-config.txt')
        path3 = os.path.join(directory, '../flavor-config.txt')
        error_flag = False
        if os.path.isfile(path1):
            if os.path.isfile(path2):
                if os.path.isfile(path3):
                    with open(path1) as file1:
                        print file1.read()
                    with open(path2) as file2:
                        print file2.read()
                    with open(path3) as file3:
                        print file3.read()
                    error_flag = True
                    log(arg2, 'SUCCESS\n')
                else:
                    print 'ERROR : Flavors information not yet configured'
            else:
                print 'ERROR : Images information not yet configured'
        else:
            print 'ERROR : Hardware information not yet configured'
        if error_flag == False:
            log(arg2, 'FAILURE\n')

    else:
        print 'ERROR : Wrong command, can only show "hardware", "images", "flavors" or "all"'
        log(arg2, 'FAILURE\n')

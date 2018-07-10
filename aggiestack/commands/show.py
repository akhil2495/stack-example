# command show

# help documentation
# commands possible :
# aggiestack show hardware ---> prints the h/w info available on cloud
# aggiestack show images   ---> prints the images available for the user to choose when creating virtual machines
# aggiestack show flavors  ---> prints the list of available flavors for the user when creating virtual machines
# aggiestack show all      ---> prints all the above messages

import os

def show_log(arg):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../aggiestack-log.txt')
    if os.path.isfile(path):
        with open(path, 'a') as file_handle:
            file_handle.write(arg)
    else:
        with open(path, 'w') as file_handle:
            file_handle.write(arg)

def show_command(arg1, arg2):
    # arg1 : hardware , images , flavors

    directory = os.path.dirname(os.path.realpath(__file__)) 
    print os.getcwd()
    if arg1 == 'hardware':
        path = os.path.join(directory, '../hdwr-config.txt') 
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
            show_log(arg2 + 'SUCCESS\n')
        else:
            print 'ERROR : Hardware information not yet configured'
            show_log(arg2 + 'FAILURE\n')

    elif arg1 == 'images':
        path = os.path.join(directory, '../image-config.txt')
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
            show_log(arg2 + 'SUCCESS\n')
        else:
            print 'ERROR : Image information not yet configured'
            show_log(arg2 + 'FAILURE\n')
            
    elif arg1 == 'flavors':
        path = os.path.join(directory, '../flavor-config.txt')
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
            show_log(arg2 + 'SUCCESS\n')
        else:
            print 'ERROR : Flavors information not yet configured'
            show_log(arg2 + 'FAILURE\n')

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
                    show_log(arg2 + 'SUCCESS\n')
                else:
                    print 'ERROR : Flavors information not yet configured'
            else:
                print 'ERROR : Images information not yet configured'
        else:
            print 'ERROR : Hardware information not yet configured'
        if error_flag == False:
            show_log(arg2 + 'FAILURE\n')

    else:
        print 'ERROR : Wrong command, can only show "hardware", "images", "flavors" or "all"'
        show_log(arg2 + 'FAILURE\n')

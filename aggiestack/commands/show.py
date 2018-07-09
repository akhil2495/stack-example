# command show

# help documentation
# commands possible :
# aggiestack show hardware ---> prints the h/w info available on cloud
# aggiestack show images   ---> prints the images available for the user to choose when creating virtual machines
# aggiestack show flavors  ---> prints the list of available flavors for the user when creating virtual machines
# aggiestack show all      ---> prints all the above messages

import os

def show_command(arg1):
    # arg1 : hardware , images , flavors

    directory = os.path.dirname(os.path.realpath(__file__)) 
    
    if arg1 == 'hardware':
        path = os.path.join(directory, '../config-files/hdwr-config.txt') 
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
        else:
            print 'Error : Hardware information not yet configured'

    elif arg1 == 'images':
        path = os.path.join(directory, '../config-files/image-config.txt')
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
        else:
            print 'Error : Image information not yet configured'

    elif arg1 == 'flavors':
        path = os.path.join(directory, '../config-files/flavor-config.txt')
        if os.path.isfile(path):
            with open(path) as file_handle:
                print file_handle.read()
        else:
            print 'Error : Flavors information not yet configured'

    elif arg1 == 'all':
        path1 = os.path.join(directory, '../config-files/hdwr-config.txt')
        path2 = os.path.join(directory, '../config-files/image-config.txt')
        path3 = os.path.join(directory, '../config-files/flavor-config.txt')
        if os.path.isfile(path1):
            if os.path.isfile(path2):
                if os.path.isfile(path3):
                    with open(path1) as file1:
                        print file1.read()
                    with open(path2) as file2:
                        print file2.read()
                    with open(path3) as file3:
                        print file3.read()

    else:
        print 'Error : Wrong command, can only show "hardware", "images", "flavors" or "all"'

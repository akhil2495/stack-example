import os

def config_command(arg1, arg2):
    # arg1 : --hardware , --images , --flavors
    # arg2 : filename

    if arg1 == 'hardware':
        #path = os.path(arg2)
        directory = os.path.dirname(os.path.realpath(__file__)) 
        path = os.path.join(directory, '../' + arg2)
        f = open(path)
        #print 'hi'
        #file_handle = open(arg2) 
        # check if command is successful or not
        print ("checking success for now")            

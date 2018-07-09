import os

def parse_flavors():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../config-files/flavor-config.txt')
    flavors = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            for line in file_handle:
                if i > 0:
                    line = line.rstrip()
                    words = line.split()
                    flavors[words[0]] = {'mem': int(words[1]), 'ndisks': int(words[2]), 'vcpus': int(words[3])}
                i += 1
    return flavors

def parse_hardware():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../config-files/hdwr-config.txt')
    hardware = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            for line in file_handle:
                if i > 0:
                    line = line.rstrip()
                    words = line.split()
                    hardware[words[0]] = {'ip': words[1], 'mem': int(words[2]), 'ndisks': int(words[3]), 'vcpus': int(words[4])}
                i += 1
    return hardware

def admin_log(arg):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../log-files/aggiestack-log.txt')
    if os.path.isfile(path):
        with open(path, 'a') as file_handle:
            file_handle.write(arg)
    else:
        with open(path, 'w') as file_handle:
            file_handle.write(arg)

def admin_show_command(arg):
    # arg : executed command

    directory = os.path.dirname(os.path.realpath(__file__)) 
    path = os.path.join(directory, '../config-files/hdwr-config.txt')
    if os.path.isfile(path):
        with open(path) as file_handle:
            print file_handle.read()
        admin_log(arg + 'SUCCESS\n')
    else:
        print 'ERROR : Hardware information not yet configured'
        admin_log(arg + 'FAILURE\n')

def admin_can_host_command(arg1, arg2, arg3):
    # arg1 : name of the hardware
    # arg2 : name of the flavor
    # arg3 : executed command

    flavors = parse_flavors()
    hardware = parse_hardware()

    # checking if the machine name is in the hardware file and if the flavor can fit
    if flavors[arg2]['mem'] > hardware[arg1]['mem']:
        print 'ERROR : Memory insufficient'
        admin_log(arg3 + 'FAILURE\n')
    elif flavors[arg2]['ndisks'] > hardware[arg1]['ndisks']:
        print 'ERROR : Not sufficient disks'
        admin_log(arg3 + 'FAILURE\n')
    elif flavors[arg2]['vcpus'] > hardware[arg1]['vcpus']:
        print 'ERROR : Not sufficient cpus'
        admin_log(arg3 + 'FAILURE\n')
    else:
        print 'yes'
        admin_log(arg3 + 'SUCCESS\n')

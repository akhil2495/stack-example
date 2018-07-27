import os

def log(arg1, arg2, arg3):
    # arg1 : executed command (or) indication of internal function call
    # arg2 : SUCCESS (or) FAILURE
    # arg3 : Message to print on screen

    if arg1:
        directory = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(directory, '../aggiestack-log.txt')
        if os.path.isfile(path):
            with open(path, 'a') as file_handle:
                file_handle.write(arg1 + arg2)
                print arg3
        else:
            with open(path, 'w') as file_handle:
                file_handle.write(arg1 + arg2)
                print arg3

def parse_hardware(arg = ''):
    # arg can be '' or 'current'
    directory = os.path.dirname(os.path.realpath(__file__))
    if arg == '':
        path = os.path.join(directory, '../hdwr-config.txt')
    elif arg == 'current':
        path = os.path.join(directory, '../server-config.txt')
    hardware = dict()
    rack = dict()
    server = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            for line in file_handle:
                if i == 0:
                    hardware['nracks'] = line.rstrip()
                    nracks = int(line.rstrip())
                if i > 0:
                    if nracks > 0:
                        line = line.rstrip()
                        words = line.split()
                        rack[words[0]] = words[1]
                    else:
                        line = line.rstrip()
                        words = line.split()
                        server[words[0]] = {'rack': words[1],'ip': words[2], 'mem': int(words[3]), 'ndisks': int(words[4]), 'vcpus': int(words[5])}
                i += 1
    hardware = {'server': server, 'rack': rack}
    return hardware

def update_hardware(hardware, racks):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../server-config.txt')
    with open(path, 'w') as file_handle:
        file_handle.write(str(len(racks.keys())))
        for key in racks.keys():
            file_handle.write(key + ' ' + racks[key])
        file_handle.write(str(len(hardware.keys())))
        current = hardware[key]
        for key in hardware.keys():
            file_handle.write(key + ' ' + current['rack']  + current['ip'] + ' ' + current['mem'] + ' ' + current['ndisks'] + ' ' + current['vcpus'])
    return

def parse_flavors():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../flavor-config.txt')
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

def parse_instances(arg):
    # arg can be 'instance2imageflavor' or 'server2instance'
    
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    instance = dict()
    server = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            temp = dict()
            for line in file_handle:
                if i > 0:
                    line = line.rstrip()
                    words = line.split()
                    if arg == 'instance2imageflavor':
                        temp['server'] = words[1]
                        temp['image'] = words[2]
                        temp['flavor'] = words[3]
                        instance[words[0]] = temp
                    elif arg == 'server2instance':
                        server[words[1]] = words[0]
    if arg == 'instance2imageflavor':
        return instance
    elif arg == 'server2instance':
        return server

def update_instances(instances):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    
    if os.path.isfile(path):
        with open(path, 'w') as file_handle:
            f.write(str(len(instances.keys())))
            for key in instances.keys():
                f.write(key + ' ' + instances[key]['server'] + instances[key]['image'] + ' ' + instances[key]['flavor'])
    return True

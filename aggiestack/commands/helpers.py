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
    return

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
            j = 0
            for lines in file_handle:
                if i == 0:
                    hardware['nracks'] = lines.rstrip()
                    nracks = int(lines.rstrip())
                if i > 0:
                    if nracks > 0:
                        line = lines.rstrip()
                        words = line.split()
                        rack[words[0]] = words[1]
                        nracks -= 1
                    else:
                        if j == 0:
                            hardware['nservers'] = line.rstrip()
                            nservers = int(lines.rstrip())
                        else:
                            line = lines.rstrip()
                            words = line.split()
                            server[words[0]] = {'rack': words[1], 'ip': words[2], 'mem': int(words[3]), 'ndisks': int(words[4]), 'vcpus': int(words[5])}
                        j += 1
                i += 1
    else:
        if arg == '':
            print 'ERROR: The hardware configuration is not yet done'
            return {}
        else:
            hardware = parse_hardware('')
            update_hardware(hardware['server'], hardware['rack'])
            return hardware
    hardware = {'server': server, 'rack': rack}
    return hardware

def update_hardware(hardware, racks):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../server-config.txt')
    with open(path, 'w') as file_handle:
        file_handle.write(str(len(racks.keys())) + '\n')
        for key in racks.keys():
            file_handle.write(key + ' ' + racks[key] + '\n')
        file_handle.write(str(len(hardware.keys())) + '\n')
        for key in hardware.keys():
            current = hardware[key]
            file_handle.write(key + ' ' + current['rack'] + ' ' + current['ip'] + ' ' + str(current['mem']) + ' ' + str(current['ndisks']) + ' ' + str(current['vcpus']) + '\n')
    return

def parse_flavors():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../flavor-config.txt')
    flavors = dict()
    if os.path.isfile(path):
        with open(path) as file_handle:
            i = 0
            for lines in file_handle:
                if i > 0:
                    line = lines.rstrip()
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
            for lines in file_handle:
                if i > 0:
                    line = lines.rstrip()
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
            for lines in file_handle:
                temp = dict()
                if i > 0:
                    line = lines.rstrip()
                    words = line.split()
                    temp['server'] = words[1]
                    temp['image'] = words[2]
                    temp['flavor'] = words[3]
                    instance[words[0]] = temp
                i += 1
    return instance

def update_instances(instances):
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../instance-config.txt')
    
    with open(path, 'w') as file_handle:
        file_handle.write(str(len(instances.keys())) + '\n')
        for key in instances.keys():
            file_handle.write(key + ' ' + instances[key]['server'] + ' ' +  instances[key]['image'] + ' ' + instances[key]['flavor'] + '\n')
    return True

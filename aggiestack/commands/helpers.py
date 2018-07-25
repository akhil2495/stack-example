import os

def log(arg1, arg2):
    if arg1:
        directory = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(directory, '../aggiestack-log.txt')
        if os.path.isfile(path):
            with open(path, 'a') as file_handle:
                file_handle.write(arg)
        else:
            with open(path, 'w') as file_handle:
                file_handle.write(arg)

def parse_hardware():
    directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(directory, '../hdwr-config.txt')
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

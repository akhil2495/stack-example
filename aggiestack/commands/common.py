from helpers import parse_hardware
from helpers import parse_flavors
from helpers import log

def admin_can_host_command(arg1, arg2, arg3 = ''):
    # arg1 : name of the hardware
    # arg2 : name of the flavor
    # arg3 : executed command

    flavors = parse_flavors()
    hardware = parse_hardware('current')
    hardware = hardware['server']

    if arg2 not in flavors.keys():
        ERR_MSG = 'ERROR : Wrong flavor name'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    if arg1 not in hardware.keys():
        ERR_MSG = 'ERROR : Wrong hardware name'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False

    # checking if the machine name is in the hardware file and if the flavor can fit
    if flavors[arg2]['mem'] > hardware[arg1]['mem']:
        ERR_MSG = 'ERROR : Memory insufficient'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    elif flavors[arg2]['ndisks'] > hardware[arg1]['ndisks']:
        ERR_MSG = 'ERROR : Not sufficient disks'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    elif flavors[arg2]['vcpus'] > hardware[arg1]['vcpus']:
        ERR_MSG = 'ERROR : Not sufficient cpus'
        log(arg3, 'FAILURE\n', ERR_MSG)
        return False
    else:
        MSG = 'yes'
        log(arg3, 'SUCCESS\n', MSG)
        return True

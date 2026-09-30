import random

def random_mac():

    mac = [
        random.randint(0x00, 0xFF) & 0xFE, 
        random.randint(0x00, 0xFF),
        random.randint(0x00, 0xFF),
        random.randint(0x00, 0xFF),
        random.randint(0x00, 0xFF),
        random.randint(0x00, 0xFF),
    ]
    return ':'.join(['%02X' % x for x in mac])

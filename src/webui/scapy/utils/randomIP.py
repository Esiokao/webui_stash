import random


def randomIP():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

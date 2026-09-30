# config.py
CONFIG = {
    "SECRET_KEY": "my_secret_key",
    "DATABASE_URL": "postgresql://user:password@localhost:5432/mydatabase",
    "ADMIN_USER_ACCOUNT": "admin1",
    "ADMIN_USER_PASSWORD": "StrongP@ssw0rd",
    "TWAMP_SERVER": {
      "ACCEPTABLE_PROTOCOLS": ['ipv4', 'ipv6'],
      "MINIMUM_UPD_PORT_RANGE": (1063, 65535),
    },
    "VLAN": {
      "VLAN_TAG_RANGE" : (2, 4094)
    },
    "PRIVATE_VLAN":{
      "VLAN_TAG_MAXIMUN": 768,
      "VLAN_TAG_RANGE": (2, 768)
    },
    # paths for mount
    "MOUNT_PATH": {
      "USECASES":"",
      "INVOKERS":"",
      "COMMANDS":""
    }
}

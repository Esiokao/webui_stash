from collections import namedtuple
from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.commands.MacBaseAccessControlCommand import MacBaseAccessControlCommand
from webui.command.utils.randomMac import random_mac


def run(crt_env):
    try:
        mac_base_access_control_command = MacBaseAccessControlCommand(crt_env)

        MacAccessTable = namedtuple("MacAccessTable", ["mac_addr", "vlan_id"])

        table_list = [MacAccessTable(mac_addr=random_mac(), vlan_id="1") for i in range(1024)]

        mac_base_access_control_command.enable()

        mac_base_access_control_command.add_mac_addr_table(table_list)

        test_invoker = TestInvoker()

        test_invoker.addCommand(mac_base_access_control_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False

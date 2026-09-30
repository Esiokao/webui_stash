from webui.command.commands.PrivateVlanCommand import PrivateVlanCommand
from webui.command.Invokers.TestInvoker import TestInvoker


def run(crt_env):
    try:
        private_vlan_command = PrivateVlanCommand(crt_env)

        vlans = [{"vlanName": "vlan" + str(i + 1), "vlanID": str(i + 1)} for i in range(1, 4094)]

        private_vlan_command.createPrivateVlan(vlans)

        test_invoker = TestInvoker()

        test_invoker.addCommand(private_vlan_command)

        test_invoker.run()

        return True

    except Exception:
        return False

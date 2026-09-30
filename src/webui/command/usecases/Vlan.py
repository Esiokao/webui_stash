from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.commands.VlanCommand import VlanCommand
from webui.command.config import CONFIG

def run(crt_env):

  try:

    vlan_command = VlanCommand(crt_env)

    vlans = [{'vlanName': 'vlan' + str(i + 1), 'vlanID' : str(i + 1)} for i in range(1, 4094)]

    vlan_command.create_vlan(vlans)

    test_invoker = TestInvoker()

    test_invoker.addCommand(vlan_command)

    test_invoker.run()

    return True

  except Exception as e:

    return False


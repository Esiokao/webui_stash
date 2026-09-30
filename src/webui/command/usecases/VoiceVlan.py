from webui.command.commands.VoiceVlanCommand import VoiceVlanCommand
from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.utils.randomMac import random_mac


def run(crtEnv):
    try:
        voice_vlan_command = VoiceVlanCommand(crtEnv)

        ouiLists = [{"macAddr": random_mac()} for _ in range(10000)]

        voice_vlan_command.addMultipleOui(ouiLists)

        testInvoker = TestInvoker()

        testInvoker.addCommand(voice_vlan_command)

        testInvoker.run()

        return True
    except Exception:
        return False

from webui.command.commands.Dot1vCommand import Dot1vCommand
from webui.command.Invokers.TestInvoker import TestInvoker
from collections import namedtuple


def run(crt_env):
    try:
        dot1v_command = Dot1vCommand(crt_env)

        Dot1vGroup = namedtuple("Dot1vGroup", ["id", "name"])

        group_list = [Dot1vGroup(id=str(i % 11), name="name" + str(i)) for i in range(10)]

        dot1v_command.addMultipleVlanGroup(group_list)

        test_invoker = TestInvoker()

        test_invoker.addCommand(dot1v_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False

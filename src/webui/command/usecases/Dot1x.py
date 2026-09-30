from webui.command.commands.Dot1xCommand import Dot1xCommand
from webui.command.Invokers.TestInvoker import TestInvoker
from collections import namedtuple


def run(crt_env):
    try:
        dot1x_command = Dot1xCommand(crt_env)

        User = namedtuple("User", ["username", "password"])

        user_list = [User(username="user" + str(i), password="pass" + str(i)) for i in range(500)]

        dot1x_command.enable()

        dot1x_command.addUser(user_list)

        test_invoker = TestInvoker.TestInvoker()

        test_invoker.addCommand(dot1x_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False

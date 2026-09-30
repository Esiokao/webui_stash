from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.commands.Reboot import RebootCommand


def run(crt_env):
    try:
        logout_command = RebootCommand(crt_env)

        test_invoker = TestInvoker()

        test_invoker.addCommand(logout_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False

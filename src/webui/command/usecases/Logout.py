from webui.command.commands.LogoutCommand import LogoutCommand
from webui.command.Invokers.TestInvoker import TestInvoker


def run(crt_env):
    try:
        logout_command = LogoutCommand(crt_env)

        test_invoker = TestInvoker()

        test_invoker.addCommand(logout_command)

        test_invoker.run()

        return True

    except Exception:
        return False

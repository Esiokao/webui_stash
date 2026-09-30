from webui.command.commands.LoginCommand import LoginCommand
from webui.command.commands.ResetCommand import ResetCommand
from webui.command.config import CONFIG
from webui.command.Invokers.TestInvoker import TestInvoker


def run(crt_env):
    try:
        # init command
        reset_command = ResetCommand(crt_env)

        login_command = LoginCommand(crt_env, CONFIG["ADMIN_USER_ACCOUNT"], CONFIG["ADMIN_USER_PASSWORD"])

        test_invoker = TestInvoker.TestInvoker()

        # add to task queue
        test_invoker.addCommand(reset_command)

        test_invoker.addCommand(login_command)

        test_invoker.run()

        return True

    except Exception:
        return False

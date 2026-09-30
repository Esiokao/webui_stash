from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.commands.LoginCommand import LoginCommand
from webui.command.config import CONFIG


def run(crt_env):
    try:
        login_command = LoginCommand.LoginCommand(crt_env, CONFIG['ADMIN_USER_ACCOUNT'], CONFIG['ADMIN_USER_PASSWORD'])

        test_invoker = TestInvoker.TestInvoker()

        test_invoker.addCommand(login_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False

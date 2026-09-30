from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.commands.ResetCommand import ResetCommand


def run(crtEnv):
    try:
        reset_command = ResetCommand(crtEnv)

        test_invoker = TestInvoker()

        test_invoker.addCommand(reset_command)

        test_invoker.run()

        return True

    except Exception as e:

        return False

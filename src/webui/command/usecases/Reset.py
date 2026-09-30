from webui.command.commands.ResetCommand import ResetCommand
from webui.command.Invokers.TestInvoker import TestInvoker


def run(crtEnv):
    try:
        reset_command = ResetCommand(crtEnv)

        test_invoker = TestInvoker()

        test_invoker.addCommand(reset_command)

        test_invoker.run()

        return True

    except Exception:
        return False

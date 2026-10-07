from webui.command.commands.ACLCommand import ACLCommand
from webui.command.Invokers.TestInvoker import TestInvoker


def run(crt_env):

    try:
        acl_command = ACLCommand(crt_env)

        acls = [{"aclID": str(i + 1)} for i in range(0, 6)]

        acl_command.create_acl(acls)

        test_invoker = TestInvoker()

        test_invoker.addCommand(acl_command)

        test_invoker.run()

        return True

    except Exception:
        return False

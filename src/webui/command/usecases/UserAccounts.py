from webui.command.commands.UserAccountsCommand import UserAccountsCommand
from webui.command.config import CONFIG
from webui.command.Invokers.TestInvoker import TestInvoker


def run(crtEnv):
    try:
        userAccountCommand = UserAccountsCommand(crtEnv)

        # must create an admin account first

        AdminAccount = [{"username": CONFIG["ADMIN_USER_ACCOUNT"], "accessRight": "admin", "password": CONFIG["ADMIN_USER_PASSWORD"]}]

        userAccountCommand.createNewUserAccount(AdminAccount)

        userAccounts = [{"username": "helloworld" + str(i), "accessRight": "user", "password": CONFIG["ADMIN_USER_PASSWORD"]} for i in range(1, 100)]

        userAccountCommand.createNewUserAccount(userAccounts)

        testInvoker = TestInvoker()

        testInvoker.addCommand(userAccountCommand)

        testInvoker.run()

        return True

    except Exception:
        return False

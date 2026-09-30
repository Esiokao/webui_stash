from webui.command.commands.SnmpCommand import SnmpCommand
from webui.command.Invokers.TestInvoker import TestInvoker
from webui.command.utils.randomIP import randomIP


def run(crtEnv):
    try:
        snmpCommand = SnmpCommand(crtEnv)

        snmpUsers = [
            {"name": "user" + str(i), "group": "group" + str(i), "version": "v" + str((i % 3) + 1), "auth": "noauth_nopriv" if ((i % 3) + 1) == 3 else None}
            for i in range(1, 51)
        ]

        # snmpCommand.createMultipleUsers(snmpUsers)

        snmpGroups = [
            {"name": "group" + str(i), "version": "v" + str((i % 3) + 1), "auth": "noauth_nopriv" if ((i % 3) + 1) == 3 else None} for i in range(1, 51)
        ]

        # snmpCommand.createMultipleGroups(snmpGroups)

        snmpViews = [{"name": "view" + str(i), "subTree": 1, "oidMask": 1, "viewType": "include"} for i in range(1, 11)]

        # snmpCommand.createMultipleViews(snmpViews)

        snmpCommunities = [{"name": "community" + str(i), "viewName": "viewName" + str(i), "accessRight": "read_write"} for i in range(1, 100)]

        # snmpCommand.createMultipleCommunities(snmpCommunities)

        snmpHosts = [{"ipAddr": randomIP(), "communityName": "public", "version": "v1"} for i in range(1, 10)]

        snmpCommand.createMultipleHosts(snmpHosts)

        testInvoker = TestInvoker()

        testInvoker.addCommand(snmpCommand)

        testInvoker.run()

        return True

    except Exception:
        return False

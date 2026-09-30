from webui.command.commands.Command import Command


class UserAccountsCommand(Command):
    def __init__(self, crtEnv):
        self.__crtEnv = crtEnv
        self.__taskList = []
        self.__acceptableAccessRights = ["admin", "operator", "power-user", "user"]

    def createNewUserAccount(self, users):
        for user in users:
            if user["accessRight"] not in self.__acceptableAccessRights:
                return
            command = "create account {accessRight} {username} ".format(accessRight=user["accessRight"], username=user["username"])
            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))
            self.__taskList.append(lambda: self.__crtEnv.waitForString("password:"))
            self.__taskList.append(lambda password=user["password"]: self.__crtEnv.send(password))
            self.__taskList.append(lambda: self.__crtEnv.waitForString("confirmation:"))
            self.__taskList.append(lambda password=user["password"]: self.__crtEnv.send(password))

    def execute(self):
        if self.__taskList:
            for task in self.__taskList:
                task()
        # clear list after all tasks had been done
        self.__taskList = []

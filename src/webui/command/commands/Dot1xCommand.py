from webui.command.commands.Command import Command

class Dot1xCommand(Command):

    def __init__(self, crtEnv):

        self.__taskList = []
        self.__crtEnv = crtEnv

    def enable(self):
        command = 'enable 802.1x'
        self.__taskList.append(lambda cmd=command: self.__crtEnv.send(cmd))

    def addUser(self, userList):
        for user in userList:
            command = 'create 802.1x user {username}'.format(username=user.username)
            self.__taskList.append(lambda cmd=command: self.__crtEnv.send(cmd))
            pwd_prompt = "password:"
            self.__taskList.append(lambda anchor=pwd_prompt: self.__crtEnv.waitForString(anchor, 60))
            self.__taskList.append(lambda pwd=user.password: self.__crtEnv.send(pwd))
            conf_prompt = "confirmation:"
            self.__taskList.append(lambda anchor=conf_prompt: self.__crtEnv.waitForString(anchor, 60))
            self.__taskList.append(lambda pwd=user.password: self.__crtEnv.send(pwd))

    def execute(self):
        if self.__taskList:
            for task in self.__taskList:
                task()
        # clear list after all tasks had been done
        self.__taskList = []


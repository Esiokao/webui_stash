from webui.command.commands.Command import Command


class LoginCommand(Command):
    def __init__(self, crtEnv, username, password):
        self.__crtEnv = crtEnv
        self.__username = username
        self.__password = password

    def execute(self):
        # self.__crtEnv.send('')
        self.__crtEnv.send("")
        self.__crtEnv.waitForString("login...", 200)
        self.__crtEnv.send("")
        self.__crtEnv.waitForString("ame:", 200)
        self.__crtEnv.sleep(1)
        self.__crtEnv.send(self.__username)
        self.__crtEnv.waitForString("assword:", 200)
        self.__crtEnv.sleep(1)
        self.__crtEnv.send(self.__password)

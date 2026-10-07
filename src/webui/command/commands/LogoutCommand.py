from webui.command.commands.Command import Command


class LogoutCommand(Command):
    def __init__(self, crtEnv):
        self.__crtEnv = crtEnv

    def execute(self):
        self.__crtEnv.send("")
        self.__crtEnv.send("")
        self.__crtEnv.send("logout")

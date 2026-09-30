from webui.command.commands.Command import Command


class RebootCommand(Command):
    def __init__(self, crt_env):

        self.__taskList = []
        self.__crtEnv = crt_env

    def execute(self):
        self.__crtEnv.send("")
        self.__crtEnv.send("")
        self.__crtEnv.send("reboot")
        self.__crtEnv.waitForString("(y/n)")
        self.__crtEnv.sleep(0.1)
        self.__crtEnv.send("y")

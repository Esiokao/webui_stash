"""
  Reset Switch Config
"""
from webui.command.commands.Command import Command


class ResetCommand(Command):
    def __init__(self, crtEnv):
        self.__crtEnv = crtEnv
        self.__timeout = 150
    def execute(self):
        self.__crtEnv.send('')
        self.__crtEnv.send('')
        self.__crtEnv.send('')
        self.__crtEnv.send('')
        self.__crtEnv.send('')
        self.__crtEnv.send('')
        self.__crtEnv.send('reset config')
        self.__crtEnv.waitForString('reset?', self.__timeout if self.__timeout else 150)
        self.__crtEnv.send('y')
        self.__crtEnv.sleep(1)
        self.__crtEnv.waitForString('Success.', self.__timeout if self.__timeout else 150)
        self.__crtEnv.sleep(3)

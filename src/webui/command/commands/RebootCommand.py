from webui.command.commands.Command import Command

class RebootCommand(Command):
  def __init__(self, crtEnv):
    self.__crtEnv = crtEnv
  def execute(self):
    self.__crtEnv.send('')
    self.__crtEnv.send('')
    self.__crtEnv.send('reboot')
    self.__crtEnv.waitForString('reboot?')
    self.__crtEnv.sleep(200)
    self.__crtEnv.send('y')
    
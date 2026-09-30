from webui.command.commands.Command import Command


class TestCommand(Command):
  def __init__(self, crtEnv):
    self.__crtEnv = crtEnv
    
  def execute(self):
    
    self.__crtEnv.send('Hello World!')
    
  
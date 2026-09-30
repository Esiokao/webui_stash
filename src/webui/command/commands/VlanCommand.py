from webui.command.commands.Command import Command

class VlanCommand(Command):
  
  def __init__(self, crtEnv):
    
    self.__taskList = []
    self.__crtEnv = crtEnv
    
  def create_vlan(self, vlans):
    
    for vlan in vlans:
      command = 'create vlan {vlanName} tag {vlanID}'.format(vlanName = vlan['vlanName'], vlanID= vlan['vlanID'])
      self.__taskList.append(lambda command=command: self.__crtEnv.send(command))  
  
  def execute(self):
    if self.__taskList:
      for task in self.__taskList:
        task()
    # clear list after all tasks had been done
    self.__taskList = []  
    

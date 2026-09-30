from webui.command.commands.Command import Command

class PrivateVlanCommand(Command):
  
  def __init__(self, crtEnv):
    
    self.__taskList = []
    self.__crtEnv = crtEnv
    
  def createPrivateVlan(self, privateVlans):
    
    for privateVlan in privateVlans:
      command = 'create vlan {vlanName} tag {vlanID} private_vlan'.format(vlanName = privateVlan['vlanName'], vlanID= privateVlan['vlanID'])
      self.__taskList.append(lambda command=command: self.__crtEnv.send(command))  
  
  def execute(self):
    if self.__taskList:
      for task in self.__taskList:
        task()
    # clear list after all tasks had been done
    self.__taskList = []  
    

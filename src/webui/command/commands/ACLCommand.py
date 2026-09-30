from webui.command.commands.Command import Command

class ACLCommand(Command):
  
  def __init__(self, crtEnv):
    
    self.__taskList = []
    self.__crtEnv = crtEnv
    
  def create_acl(self, acls):

    for acl in acls:
      command = 'create access_profile ethernet ethernet_type profile_id {aclID}'.format(aclID= acl['aclID'])
      self.__taskList.append(lambda command=command: self.__crtEnv.send(command))  
  
  def execute(self):
    if self.__taskList:
      for task in self.__taskList:
        task()
    # clear list after all tasks had been done
    self.__taskList = []  
    

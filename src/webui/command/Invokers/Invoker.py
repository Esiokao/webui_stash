class Invoker(object):
  
  def __init__(self):
    
    self.__commandList = []
  
  def addCommand(self, command):
    self.__commandList.append(command)
    
  def run(self):
    for command in self.__commandList:
      command.execute()
  
  
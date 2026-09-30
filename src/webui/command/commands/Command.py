from abc import abstractmethod

class Command(object):
  
  @property
  def __taskList(self):
    return self.__taskList
  
  @abstractmethod
  def execute(self):
    pass
  
  
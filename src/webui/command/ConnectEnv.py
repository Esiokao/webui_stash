class CrtEnv:

  # adapter

  def __init__(self, crtAPI):
    self.__tab = None
    self.__crt = crtAPI

  def messageBox(self, msg, title):
    return self.__crt.Dialog.MessageBox(msg, title)

  def promptBox(self, msg, title):
    return self.__crt.Dialog.Prompt(msg, title, "", False)

  def inputBox(self, msg, title):
    return self.__crt.Dialog.Prompt(msg, title, "", True)

  def __checkEnv(self):
    if self.__isTabEmpty():
      self.__getCurrentTab()
      self.__tab.Screen.Synchronous = True

  def __getCurrentTab(self):
    self.__tab = self.__crt.GetScriptTab()

  def __isTabEmpty(self):
    return self.__tab == None

  def send(self, msg):
    self.__checkEnv()
    self.__send(msg)

  def __send(self, msg):
    msg = msg + '\n'
    self.__tab.Screen.Send(msg)

  def waitForString(self, string, timeout=5):
    self.__tab.Screen.WaitForString(string, timeout)

  def sleep(self, miliseconds):
    self.__crt.Sleep(miliseconds)
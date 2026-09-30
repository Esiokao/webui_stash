from webui.command.commands.Command import Command


class VoiceVlanCommand(Command):
    def __init__(self, crtEnv):

        self.__taskList = []
        self.__crtEnv = crtEnv

    def enable(self, vlanID):
        command = "enable voice_vlan vlanid {vlanID}".format(vlanID=vlanID)
        self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def addMultipleOui(self, ouiLists):

        for ouiList in ouiLists:
            command = "config voice_vlan oui add {macAddr}".format(macAddr=ouiList["macAddr"])
            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def execute(self):
        if self.__taskList:
            for task in self.__taskList:
                task()
        # clear list after all tasks had been done
        self.__taskList = []

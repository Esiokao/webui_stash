from webui.command.commands.Command import Command


class QinQCommand(Command):
    def __init__(self, crtEnv):

        self.__taskList = []
        self.__crtEnv = crtEnv

    def enable(self):
        command = "enable qinq"
        self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def addVlanTranslationCVID(self, vidLists):

        for vidList in vidLists:
            command = "create vlan_translation ports all {_action} cvid {_cvid} svid {_svid} priority {_priority}".format(
                _action=vidList["action"], _cvid=vidList["cvid"], _svid=vidList["svid"], _priority=vidList["priority"]
            )
            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def execute(self):
        if self.__taskList:
            for task in self.__taskList:
                task()
        # clear list after all tasks had been done
        self.__taskList = []

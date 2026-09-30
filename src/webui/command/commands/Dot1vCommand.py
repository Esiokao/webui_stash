from webui.command.commands.Command import Command


class Dot1vCommand(Command):
    def __init__(self, crtEnv):

        self.__taskList = []
        self.__crtEnv = crtEnv
        self.pre = False

    def addMultipleVlanGroup(self, groups):

        for group in groups:
            command = f"create dot1v_protocol_group group_id {group.id} group_name {group.name}"

            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def execute(self):
        if self.__taskList:
            for task in self.__taskList:
                task()
        # clear list after all tasks had been done
        self.__taskList = []

from webui.command.commands.Command import Command


class MacBaseAccessControlCommand(Command):
    def __init__(self, crtEnv):

        self.__taskList = []
        self.__crtEnv = crtEnv

    def enable(self):
        command = "enable mac_based_access_control"
        self.__taskList.append(lambda cmd=command: self.__crtEnv.send(cmd))

    def add_mac_addr_table(self, tableList):
        for table in tableList:
            command = "create mac_based_access_control_local mac_address {mac_addr} vlanid {vlan_id}".format(mac_addr=table.mac_addr, vlan_id=table.vlan_id)
            self.__taskList.append(lambda cmd=command: self.__crtEnv.send(cmd))

    def execute(self):
        if self.__taskList:
            for task in self.__taskList:
                task()
        # clear list after all tasks had been done
        self.__taskList = []

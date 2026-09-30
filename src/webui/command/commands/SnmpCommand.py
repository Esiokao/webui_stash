from webui.command.commands.Command import Command
class SnmpCommand(Command):
    def __init__(self, crtEnv):
        self.__taskList = []
        self.__crtEnv = crtEnv

    def createUser(self, userObj):
        command = ''
        if not userObj['auth']:

            command = 'create snmp user {name} {group} {version}'.format(name=userObj['name'], group=userObj['group'],
                                                                         version=userObj['version'])
        else:

            command = 'create snmp user {name} {group} {version} {auth}'.format(name=userObj['name'],
                                                                                group=userObj['group'],
                                                                                version=userObj['version'],
                                                                                auth=userObj['auth'])

        self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def createMultipleUsers(self, users):
        # receive multiple users
        for userObj in users:
            # run as much time as users.length
            if not userObj['auth']:

                command = 'create snmp user {name} {group} {version}'.format(name=userObj['name'],
                                                                             group=userObj['group'],
                                                                             version=userObj['version'])
            else:

                command = 'create snmp user {name} {group} {version} {auth}'.format(name=userObj['name'],
                                                                                    group=userObj['group'],
                                                                                    version=userObj['version'],
                                                                                    auth=userObj['auth'])

            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def createGroup(self, groupObj):

        if groupObj['auth']:

            command = 'create snmp group {name} {version} {auth}'.format(name=groupObj['name'],
                                                                         version=groupObj['version'],
                                                                         auth=groupObj['auth'])


        else:

            command = 'create snmp group {name} {version}'.format(name=groupObj['name'], version=groupObj['version'])

        self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def createMultipleGroups(self, groups):

        for group in groups:

            if group['auth']:

                command = 'create snmp group {name} {version} {auth}'.format(name=group['name'],
                                                                             version=group['version'],
                                                                             auth=group['auth'])

            else:

                command = 'create snmp group {name} {version}'.format(name=group['name'], version=group['version'])

            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    # TODO: community

    def createMultipleCommunities(self, communities):

        for community in communities:
            command = 'create snmp community {communityName} view {viewName} {accessRight}'.format(
                communityName=community['name'], viewName=community['viewName'], accessRight=community['accessRight'])

            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    # TODO: view

    def createMultipleViews(self, views):

        for view in views:
            command = 'create snmp view {viewName} {subTree} {oidMask} view_type {viewType}'.format(
                viewName=view['name'], subTree=view['subTree'], oidMask=view['oidMask'], viewType=view['viewType'])

            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    # TODO: host

    def createMultipleHosts(self, hosts):

        for host in hosts:

            if host['version'] is 'v3c':
                pass

            command = 'create snmp host {ipAddr} {version} {communityName}'.format(ipAddr=host['ipAddr'],
                                                                                   version=host['version'],
                                                                                   communityName=host['communityName'])

            self.__taskList.append(lambda command=command: self.__crtEnv.send(command))

    def execute(self):
        for task in self.__taskList:
            task()
        # clear list after all tasks had been done
        self.__taskList = []

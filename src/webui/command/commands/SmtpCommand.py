from webui.command.commands.Command import Command


class SmtpCommmand(Command):
    def __init___(self):
        super().__init__()
        sel.__taskList = []
        # maybe here can be replaced with a mq?

    def execute(self):

        if self.__taskList:
            for task in self.__taskList:
                task()

        # clear task list after job got done
        self.__taskList = []

#duck typing
class pycharm:
    def execute(self):
        print("compiling")
        print("running")

class myeditor:
    def execute(self):
        print("compiler")
        print("running")
        print("convenction checker")

class laptop:
    def code(self, ide):
        ide.execute()

ide = myeditor()

lap1 = laptop()
lap1.code(ide)

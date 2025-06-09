from builtins import staticmethod

global_var='I am global variable'
class staticmethod:
    class_var='I am instance variable'

    def __init__(self,instance_var):
        self.instance_var=instance_var

    @staticmethod
    def display():
        local_var='I am local variable'
        print(local_var+' is the local variable')
        print('static/class variable is ',staticmethod.class_var)
       # print('Instance Variable is ',self.instance_var)

obj=staticmethod(10)
obj.display()
staticmethod.display()
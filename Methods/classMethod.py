from builtins import classmethod

global_var='I am global variable'
class classmethod:
    class_var='I am class variable'
    def __init__(self,instance_var):
         self.instance_var=instance_var

    @classmethod
    def display(cls):
        local_var='I am local variable'
        print('Local variable is ',local_var)
        print('Global variable is ',global_var)
        print('Class variable ',cls.class_var)
        #print('Instance Variable ',self.instance_var) cannot be used

obj=classmethod('abc')
obj.display()
print('==========')
classmethod.display()


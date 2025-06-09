global_var=300 #Global Variable
class Example:
    class_var='I am a class variable' #Class Variable

    #Constructor
    def __init__(self,value):
        #Instance variable
        self.instance_var=value

    #Method
    def show_Variable(self):
        local_var='I am local Variable'
        print('Local Variable ',local_var)
        print('Instance Variable ',self.instance_var)
        print('Class Variable ',Example.class_var)
        print('Global Variable ',global_var)

# Usage:
obj1=Example(10)
obj1.instance_var=20
obj1.class_var='nikshu'
obj1.show_Variable()

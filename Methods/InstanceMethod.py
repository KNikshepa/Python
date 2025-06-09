global_var='I am global variable'
class instanceVariable:
    class_var='I am class variable'

    def __init__(self,name):
        self.name=name

    def greet(self):
        local_var='I am local variable'
        print('Local Variable ',local_var)
        print('Global Variable ',global_var)
        print('Class Variable ',instanceVariable.class_var)
        print('Instance Variable ',self.name)

obj=instanceVariable('nikshu')
obj.greet()
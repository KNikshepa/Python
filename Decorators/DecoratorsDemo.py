#Precondition to learn Decorators
from numpy.ma.core import inner
#Function Alias
def f1():
    print('f1 is printed')
f1()
f=f1
f()

#Nested function- Function inside another function
def outer():
    print('Outer function started')
    def inner():
        print('Inner function started from outer function')
    inner()
    print('Outer Function ended')
outer()

#Function as a return value
def outer1():
    print('Outer function started')
    def inner1():
        print('Inner Function stared from outer function')
    return inner1
outer1()

#Function inside another function
def send_email():
    print('Email has been sent successfully')
def notify(action):
    action()
notify(send_email())




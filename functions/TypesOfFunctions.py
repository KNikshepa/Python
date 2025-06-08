# First-Class Function
# You can assign functions to variables
# You can pass them as arguments
# You can return them from other functions
def first_class_func(name):
    return name
firstclassvar=first_class_func
print(firstclassvar('Nikshu12345'))

# First-Order Function
# A first-order function is a regular function that does NOT take another
# function as an argument and does NOT return another function.
def add(a, b):
    return a + b

# Higher-Order Function
# A higher-order function either:
# Takes another function as an argument
# OR returns a function
def sqr(x):
    return x*x
def apply_function(func,value):
    return func(value)
print(apply_function(sqr,3))
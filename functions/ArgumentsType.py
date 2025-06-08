#Positional Arguments
def positional_arguments(a,b):
    print(a/b)
positional_arguments(10,20)
# positional_arguments(20,0) ZeroDivisionError: division by zero

#Keyword Arguments
def keyword_arguments(a,b):
    print(a/b)
keyword_arguments(b=20,a=10)
keyword_arguments(b=10,a=0)

#Default Arguments
def default_arguments(name='sanu',greetmsg='Hello'):
    print(f"{greetmsg} my dear {name}")
default_arguments()
default_arguments('ramu','Hi')

#Variable Length Arguments -*args → Accepts any number of positional arguments (like a list).
def variable_length_arguments(*names):
    for name in names:
        print(f'Hello :{name}')
variable_length_arguments("Alice", "Bob", "Charlie")

#Keyword Variable Length Arguments: **kwargs → Accepts any number of keyword arguments (like a dictionary).
def keyword_variable_length_arguments(**details):
    print('keyword variable length arguments')
    for key, value in details.items():
        print(f"{key}: {value}")
details = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}
keyword_variable_length_arguments(**details)

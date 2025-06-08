def send_emailnow(func):
    def wrapper():
        result = func()  # call generate_report()
        print('Sending an email')
        return result  # return whatever generate_report() returns
    return wrapper  # return the wrapper function

# Decorator 2
def greet(func):
    def wrapper():
        print("Hello! Welcome.")
        return func()  # call the original function
    return wrapper

@greet
@send_emailnow
def generate_report():
    print('Generate the report!!!')

generate_report()


a="nikshu" if 10>5 else "Indira"
print(a)

marks=85
grade="A" if marks>=90 else "B" if marks>=75 else "C"
print(grade)

def greet(person):
    return f"Hello, {person}"

def default_greet():
    return "Hello, Guest"

name = ""
message = greet(name) if name else default_greet()
print(message)  # Output: Hello, Guest

nums = [1, 2, 3, 4, 5]
result = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(result)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

max_fn = lambda x, y: x if x > y else y
print(max_fn(10, 15))  # Output: 15
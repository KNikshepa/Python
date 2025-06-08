def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2

# Create generator object
squares = square_generator(5)

# Use the generator one value at a time
for sq in squares:
    print(sq)

squares = square_generator(5)
print(next(squares))  # 1
print(next(squares))  # 4
print(next(squares))  # 9

def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print('========')
def count_up_to_3():
    for i in range(1, 4):
        yield i
print(count_up_to_3())
print('========')
def count_up_to_3():
    for i in range(1, 4):
        yield i
gen = count_up_to_3()  # Create generator object
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# After this, calling next(gen) again will raise StopIteration

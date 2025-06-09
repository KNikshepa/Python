#1. Closure with nonlocal (Your original version)
def counter():
    count=0
    def increment():
        nonlocal count
        count+=1
        return count
    return increment

c=counter()
print(c())
print(c())
print(c())

#2. Using a Class (Clean, object-oriented)
class Counter:
    def __init__(self):
        self.count=0

    def increment(self):
        self.count+=1
        return self.count
c1=Counter()
print(c1.increment())
print(c1.increment())


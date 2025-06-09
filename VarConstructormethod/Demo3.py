count = 0
def counter():
    global count
    count += 1
    return count

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

def counter():
    counter.count += 1
    return counter.count

counter.count = 0

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3

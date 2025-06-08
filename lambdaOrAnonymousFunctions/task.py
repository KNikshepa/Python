# Filter even numbers
# Square them
# Sum the result
from functools import reduce

#List
numbers = [1, 2, 3, 4, 5, 6]
#1st way - List Comprehension
result=sum([x**2 for x in numbers if x%2==0])
print(result)
#2nd way using filter, reduce & map
evens=filter(lambda x:x%2==0,numbers)
squares=map(lambda x:x**2,evens)
result1=reduce(lambda a,b:a+b,squares)
print(result1)

# #Tuples
# numbers1= (1, 2, 3, 4, 5, 6,2,2,None)
# #1st way - List Comprehension
# result3=sum([x**2 for x in numbers1 if x%2==0])
# print(result3)
# #2nd way using filter, reduce & map
# evens1=filter(lambda x:x%2==0,numbers1)
# squares1=map(lambda x:x**2,evens1)
# result2=reduce(lambda a,b:a+b,squares1)

# Tuples
numbers1 = (1, 2, 3, 4, 5, 6, 2, 2, None)
# 1st way - List Comprehension with check
result3 = sum([x**2 for x in numbers1 if x is not None and x % 2 == 0])
print(result3)
# 2nd way - filter, map, reduce with check
evens1 = filter(lambda x: x is not None and x % 2 == 0, numbers1)
squares1 = map(lambda x: x**2, evens1)
result2 = reduce(lambda a, b: a + b, squares1)
print(result2)

result3 = sum([x**2 for x in numbers1 if isinstance(x, int) and x % 2 == 0])

#Set
numbers2 = {1, 2, 3, 4, 5, 6}
#1st way-List Comprehension
result5=sum([x**2 for x in numbers2 if x%2==0])
print(result5)
result6=reduce(lambda a,b:a+b,map(lambda a:a**2,filter(lambda a:a%2==0,numbers2)))
print(result6,"result6")

#Dictionary
data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Using list comprehension
result7=sum([v**2 for v in data.values() if v%2==0])
print(result7)
# Using filter + map + reduce
evens = filter(lambda x: x % 2 == 0, data.values())  # → [2, 4]
squares = map(lambda x: x**2, evens)                 # → [4, 16]
result1 = reduce(lambda a, b: a + b, squares)        # 4 + 16 = 20
print(result1)

ata = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Using list comprehension with .items()
result = sum([v**2 for k, v in ata.items() if k < 'd' and v % 2 == 0])
print("With .items() + List comprehension:", result)

# Using filter + map + reduce with .items()
filtered = filter(lambda item: item[0] < 'd' and item[1] % 2 == 0, ata.items())
squares = map(lambda item: item[1]**2, filtered)
result1 = reduce(lambda a, b: a + b, squares)
print("With .items() + filter/map/reduce:", result1)
# item[0] is the key (like 'a', 'b', etc.)
# item[1] is the value (like 1, 2, etc.)
s={}
print(s)
print(type(s))
s1={10,}
# print(type(s1))
# s2=eval(input('enter the data:'))
# print(s2)
s3=set(range(10))
print(s3)
s4={40,23,50,12,14,100}
s4.add(123)
s4.update([200,202,201])
print(s4)
s5=s4.copy()
s4.add(500)
print(s4)
print(s5) #Both are independent

#Pop- Remove and return a random element
print(s4.pop())
#Remove
print(s4.remove(40)) #removes 40 from s4; returns None
# Sets are unordered collections, so elements print in any order.
# .pop() removes arbitrary elements (not necessarily the first added).
# .remove() returns None but raises KeyError if element is absent.
# .discard() removes an element but doesn’t raise an error if it’s absent.
print(s4.discard(123))
s4.clear()

x={10,20,30,40}
y={30,40,50,60}
#Union
print(x.union(y))
#Intersection
print(x.intersection(y))
#Difference
print(x.difference(y))
print(y.difference(x))
# Symmetric-Element in x or y but not in both
print(x.symmetric_difference(y))
print(300 in x)
print(30 in x)

#Set Comprehension
s11={10,30,3,40}
s10={x for x in s11}
for s in s10:
    print(s)
s12 = set(map(lambda x: x*x, s11))
s13 = {x*x for x in s11}
# Set comprehension (s13) is generally preferred because it's clearer and more Pythonic.
# map with lambda is also fine, especially if you already like using functional programming tools.
s={2*x for x in range(5)}

d1={}
print(type(d1))
d2=dict()
print(type(d2))
d3={}
d3[100]="Rashi"
d3[200]="Nikshu"
d3[300]="Rani"
d4={100:'Rashi',300:'Sahu',400:'Ram'}
print(d4)
print(d4[100])
#print(d2[200]) #KeyError: 200

if 200 in d4:
    print(d4[200])
else:
    print('Invalid Key')
#del a key & value
del d4[300]
print(d4)
d4.clear()
print(d4) #empty {}
del d4
#print(d2) NameError

#Important functions in Dictionary:
d5={10:'Aanju',20:'Poorni',30:'Sanju',60:'Raju'}
print(d5)
print(len(d5))
print(d5.get(20))
print(d5.get(3000)) #When key not available it returns None
print(d5.get(60, 1))     # Will print the value for key 60 if it exists, otherwise 1
print(d5.get(44040, 12)) # Will print the value for key 44040 if it exists, otherwise 12
print(d5.pop(10))
print(d5.popitem()) #random one

print(d5.keys())
print(d5.values())
print(d5.values())

d6=d5.copy()
print(d6)
d6.update({102:'deva',103:'sonia'})
print(d6)

#Dictionary Comprehension
roll_nos = [101, 102, 103]
names = ['Ravi', 'Anu', 'John']

# Using zip + dictionary comprehension
students = {roll: name for roll, name in zip(roll_nos, names)}
print(students)
data = [(101, 'Ravi'), (102, 'Anu'), (103, 'John')]
students = {roll: name for roll, name in data}
print(students)
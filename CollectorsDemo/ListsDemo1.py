list1=[]
print(type(list1))
print(list1)
list2=[1,5.67,True,'cat',67.89,2,None]
print(list2)
#list3=eval(input('Enter the data:'))
#print(type(list3))
list4=list(range(10))
print(list4)
s='Learning Python is very easy!!!'
list5=s.split()
print(list5)

#Accessing the element through Index
list2=['Madhavi','Radha',1,2,34,7272772727277,1,None]
print(list2[0])
print(list2[len(list2)-1])
#print(list2[8]) IndexError: list index out of range
print(list2[2:5])
print(list2[-1:-12:-1])

#List is mutable
list2[2]='Roshini'
print(list2)

#Traversing of a List
#Way 1- While loop
print('=================')
list1=['Madhavi','Radha',1,2,34,7272772727277,1,None]
i=0
while i<len(list1):
    print(list1[i])
    i+=1
print('=================')
for list in list1:
    print(list)

print(len(list2))
list3=[20,40,20,20,50]
print(list3.count(20))

#Append = Append at the end
list3.append(90)
print(list3)

#insert
list3.insert(2,100)
print(list3)

#Add multiple objects
list3.extend([101,81,'nikshu'])
print(list3)

#remove
list3.remove('nikshu')
print(list3)

#Pop
list3.pop()
print(list3)
list6=[56,23,100,34,20]
list6.pop(1)
print(list6)

#Reverse
list10=[20,40,10,70,90,None,100]
list10.reverse()
print(list10)

#Sort
#print(list10.sort()) TypeError: '<' not supported between instances of 'NoneType' and 'int'
list11=['jackfruit','bannana','straberry','Apple']
list12=[50,20,30,70,80,5]
list11.sort()
print(list11)
list11.sort(reverse=True)
print(list11)

#Sort the list which is mix of int and string
sample_list = [100, 'Nikshu', 30, 50, 40, 'Indira', 20, 10]
def custom_sort_key(x):
    if isinstance(x,int):
        return 0,x  # Integers come first, sorted by value
    elif isinstance(x,str):
        return 1,x   # Strings come next, sorted alphabetically
    else:
        return 2,str(x)  # Other types (if any), converted to string
sample_list.sort(key=custom_sort_key)
print(sample_list)

#clear
print(sample_list)
sample_list.clear()
print(sample_list)

#Removing multiple objects
list1 = [10, 20, 30, 80, 4, 5, 20]
items_to_remove = [20, 80, 4, 5]
for item in items_to_remove:
    if item in list1:
        list1.remove(item)
print(list1) #Only 1 20 is removed

result=[x for x in list1 if x not in items_to_remove]
print(result)


for item in items_to_remove:
    while item in list1:
        list1.remove(item)

#Aliasing
y=[10,20,5,70]
x=y
y[1]=12.56
print(x)
print(y)
x[3]=28
print(x)
print(y)

#Cloning
x=[20,10,30,100,1,2]
y=x[:]
x[1]=464674
print(x)
print(y)

#Operator
x=[10,20,30,50]
y=[2,4,6]
print(x+y) #concat
print(y*2) #twice it prints

#Membership operator
print(10 in x)
print(10 not in x)

#Nested List
my_list=[10,[30,40],[50,80,90]]
print(my_list)
print(my_list[1])
print(my_list[1][0])
print(my_list[1:2])
print(my_list[1:3])
#It includes index start
#It excludes index end (i.e., goes up to end - 1)

#List Compression
print([x*x for x in range(5)])
list23=[x*x for x in range(10) if x%2==0]
print(list23)
words=['Apple','Grapes','Bannana','Orange']
s=[word[0] for word in words]
print(s)

#Map
numbers=[10,30,20,100,5]
def square(x):
    return x*x
del list
result = list(map(square, numbers))
print(result)

#2nd way
way2=list(map(lambda x:x*x,numbers))
print(way2)

#Filter
numbers1=[1,2,3,4,5,6,7,8]
def is_even(x):
    if x%2==0:
        return x
way1=list(filter(is_even,numbers1))
print(way1)

#2nd way
way3=list(filter(lambda x:x%2==0,numbers1))
print(way3)

#Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
way4=list(zip(names,ages))
print(way4)

for name,age in way4:
    print(f"Name is {name} & age is {age}")

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = [True, False, True]
zipped = list(zip(a, b, c))
print(zipped)

for aa,bb,cc in zipped:
    print(f"{aa},{bb},{cc}")






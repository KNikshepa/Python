from itertools import count

t=()
print(t)
print(type(t))
t1=(10)
print(t1)
print(type(t1))
t2=(20,)
t3=tuple(range(10))
print(t3)
# t4=eval(input('Input your data:'))
# print(t4)

s="Python is a very easy prog language"
print(s)
s1=s.split() #converts into list
print(s1)
s2=tuple(s1)
print(s2)

#Accessing through index
s3=(100,50,101,80,132)
print(s3[1])
print(s3[1:3])
#s3[1]=1282 TypeError: 'tuple' object does not support item assignment

#Operator
s4=(2,4,6,6,8,'nik','ind')
s5=(7,9)
print(s4+s5)
print(s5*2)
#length
print(len(s4))
print(s4.count(6))
print(s4.count('nik'))

#index
print(s4.index(6))

#Sorted
s6=(2,10,5,4,8,8,None,'Nikshu','gsk')
s7=(10,20,5,90,4)
print(sorted(s7))
print(sorted(s7,reverse=True))
print(max(s7))
print(min(s7))

def sort_logic(x):
    if isinstance(x,int):
        return 0,x
    elif isinstance(x,str):
        return 1,x
    else:
        return 2,str(x)
sorted_s6=sorted(s6,key=sort_logic)
print(sorted_s6)

#Tuple Packing & Unpacking
a=10
b=20
s7=a,b
print(s7)

t1=(10,20,30)
d,e,f=t1
print(d)  # 10
print(e)  # 20
print(f)  # 30

#Tuple Comprehension
s8=(1,1,4,5,8,2)
s9=tuple(x*x for x in s8)# This is a generator, not a tuple if tuple was not included
print(s9)
for x in s9:
    print(x)
print(type(s9))

s10=(10,5,8,20,40)
s11=tuple(map(lambda x:x,s10))
print(s11)
s12=tuple(map(lambda x:x*x,s10))
print(s12)
s13=tuple(filter(lambda x:x%2==0,s10))
print(s13)





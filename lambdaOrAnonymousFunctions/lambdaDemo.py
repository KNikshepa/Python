#Sqaure of Number
def square(x):
    print(x*x)
square(20)
sqr=lambda a:a*a
print(sqr(10))

#Greater of 2 numbers
def greateroftwo(a,b):
    if a>b:
        print(f'{a} is greater than {b}')
    else:
        print(f'{b} is greater than {a}')
greateroftwo(20,5)
greaterof2=lambda a,b:a if a>b else b
print(greaterof2(10,20))
greaterof2way=lambda a,b:print(f'{a} is greater than {b}') if a>b else print(f'{b} is greater than {a}')
greaterof2way(30,10)

#Filter
filters=[0,5,10,15,20,25,30,4,6,9]
for filter1 in filters:
    if filter1%5==0:
        print(filter1)
filtersinlambda=list(filter(lambda x:x%5==0,filters))
print(filtersinlambda)

from functools import reduce
nums = [1, 2, 3, 4, 5]
result=reduce(lambda a,b:a+b,nums)
print(result)

nums = [100, 24, 35, 89, 12]
max_num = reduce(max, nums)
print(max_num)  # Output: 100

nums = [100, 24, 35, 89, 12]
max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num)  # Output: 100

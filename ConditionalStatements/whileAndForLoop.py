n=1234
rev=0
while n>0:
    digit=n%10 #Reminder last digit
    rev=rev*10+digit
    n=n//10 #Remaining digits
print('Reversed no is ',rev)

i=0
while i<=10:
    print(i)
    i+=1

i=0
while i<=10:
    if i%2==0:
        print(f"{i} is the even no")
    else:
        print(f"{i} is the odd number")
    i+=1

i=0
while i<=10:
    if i==5:
        break
    else:
        print(i)
    i+=1

# You can use break, continue, and pass inside an if only when the if is inside a loop (for or while).
print('==============1')
i = 0
while i <= 10:
    if i == 5:
        i += 1    # 👈 increment before continue
        continue
    else:
        print(i)
    i += 1
print('==============2')

age=23
if age>18:
    pass
else:
    print("Age is less than 18")
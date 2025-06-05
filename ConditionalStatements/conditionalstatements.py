x=10
if x<20:
    print(x)

x=30
y=50
if y>x:
    print('Y is greater than X')
else:
    print('X is greater than Y')

p=30
q=40
r=10
if p>q and p>r:
    print('p is greater than q & r')
elif q>p and q>r:
    print('q is greater than p & r')
else:
    print('r is greater than p & q')

greatest = p if p > q and p > r else q if q > r else r
print("Greatest number is:", greatest)

a = 30
b = 50
c = 10
greatest = max(a, b, c)
print("Greatest number is:", greatest)

salary=91000
expense=90000
if salary>=91000:
    if expense<60000:
        print('You can save remaining amount and buy a house')
    else:
        print('try to save a bit more to be eligible')
else:
    print('your not eligible due to your salary')
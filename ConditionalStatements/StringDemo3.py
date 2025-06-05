s1='hello'
s2='nikshu'
s3=s1+s2
print(s3)
s4=s1*2
print(s4)
print('h' in s1)
print('h' not in s1)
s3="hello"
print(s2==s3)
print(s1==s3)
print(s1 is s3)
print(s1 is not s3)

#Remove the spaces in the string
# rstrip()
# lstring()
# string()
s7='   Hello nikshu your unlucky person in this world!!!  '
print(s7.rstrip())
print(s7.lstrip())
print(s7.strip())

#Comparision of 2 strings
print('Comparision of 2 strings')
print(ord('J'))
print(ord('*'))
print(chr(74))
print(chr(42))
s8='Nikshu'
s9='Nikshepa'
print(s8<s9)
print(s8>s9) #compares the first character

#Find Substrings
# Can be done using find(),index(),rfind(),rindex()
# Find() --> index of the first occurrence of the Substring --> If not found it returns -1
# index() --> same as find() --> Error if the substring is not found
s10='Python is very very simple lang'
print(s10.find('very'))      # Output: 10 (first 'very')
print(s10.rfind('very'))     # Output: 15 (last 'very')
# print(s10.index('very well'))  # ❌ Would raise ValueError since 'very well' is not in s10

#No of times substring occurred.
print(s10.count('very'))

#Replace
s11='Python is very easy language'
print(s11.replace('easy','difficult'))

#Spliting the string
s12='25/05/2025'
s13=s12.split('/')
print(s13)

#Join
s14=['abc','def','xyz','pqr']
s15='-'.join(s14)
print(s15)

print(s1.lower())
print(s1.upper())
print(s1.swapcase())
print(s1.title())
print(s1.capitalize())

#String formatting
name="Mohan"
salary=25000
location='Bangalore'
print(f"My name is {name},salary is {salary} & location is {location}")
print("My name is {}, salary is {} & location is {}".format(name,salary,location))
print("My name is {0}, salary is {1} & location is {2}".format(name,salary,location))
print("My name is {x}, salary is {y} & location is {z}".format(x=name,y=salary,z=location))


str1="Hello"
str2="""hello
world
python"""
print(str1)
print(str2)

#Accessing the element
str3="Nikshepa"
print(str3[0])
print(str3[len(str3)-2]) #p
print(len(str3)) #8
for sr in str3:
    print(sr)
print('=====')
print(str3[-1])
#print(str3[8]) #IndexError: string index out of range

#Slice Operator
print('Slice Operator in Python')
str5="Learning python is very easy task!! What do you think guys"
# str[Start index:end index:step]
print(str5[1:7:1])
print(str5[1:7:3])
print(str5[:8])
print(str5[9:])
print(str5[:])
print(str5[1:100000:1])
print(str5[::-1])

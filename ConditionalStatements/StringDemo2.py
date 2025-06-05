str1="nikshepa123"
print(str1.isalnum()) #a-z, A-Z and 0-9
str2="nikshu$"
print(str2.isalnum())

str3="indira"
str4="272772"
print(str3.isnumeric())
print(str4.isnumeric())
print(str3.isdigit())
print(str4.isdigit())
print(str1.isalpha())
print(str1.islower())
str5='NKS'
print(str5.isupper())
print("Hello World".istitle())     # ✅ True
print("Hello world".istitle())     # ❌ False (second word not capitalized)
print("Python".istitle())          # ✅ True
print("PYTHON".istitle())          # ❌ False (all caps)
print("".istitle())                # ❌ False (empty string)
print("   ".isspace())             # ✅ True (only spaces)
print("\t\n".isspace())            # ✅ True (tab + newline)
print(" Hello ".isspace())         # ❌ False (contains non-space characters)
print("".isspace())                # ❌ False (empty string)

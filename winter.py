print("hey winter")
# double division
print(90 // 3)
print(90 % 3)
a = 5
a += 2
print(a)
# multi line string
long_string = '''
wow
ooo
---
'''
print(long_string)

first_name = 'parth'
last_name = 'salunke'
full_name = first_name + " " + last_name
print(full_name)

# string concatenation
print("parth " + "salunke")

# type
print((type(str(100))))

# type conversion
x = str(100)
y = int(x)
z = type(y)
print(z)

# escape sequence for"'  for that use \ --for tab use \t for new line \n
print("\t hey parth it's\"hey\" ram \n \t good to know u")

# formatted  string using "f"  in front of print
name = "parth"
age = 20
print(f"hey {name} how are u . ur age is {age}")
print("hey {} how are u . ur age is {}".format(name, age))
print("hey {1} how are u . ur age is {0}".format(name, age))
print("hey {new_name} how are u . ur age is {age}".format(new_name="winter", age=100))

# index value of given []  [start:end]   sllicing- step over[start:stop:step ovr]
parth = "hey parth"
print(parth[4])
print(parth[0:4])
print(parth[0:7:2])
print(parth[1:])
print(parth[:5])
print(parth[::2])
print(parth[-1])
print(parth[::-1])
# immuntability we cant change index value for change the value,it is immuntability we have to make whlole new string
print(round(8))

# len
l = 'parth'
print(len('parth'))
# 12345
print(len(l))
print(l[1])
print(len('parth'))

#bool
name="parth"
ssa= True
ssa=False
print(True)







#3. Swap two numbers using a third variable and do the same task without using any third variable.
a = 556
b = 330
print(f"Before swapping: a = {a} , b= {b}")

temp = a
a = b
b = temp
print(f"After swapping: a = {a} , b= {b}" )


#Swap two numbers without using a third variable

a = 556
b = 330

print(f"Before swapping: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
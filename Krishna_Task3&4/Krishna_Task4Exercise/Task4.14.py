#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.

numbers = [1, 7, 14, 21, 28, 35, 42, 49]
result = filter(lambda x: x % 3 != 0 and x % 7 == 0, numbers)
print(list(result))


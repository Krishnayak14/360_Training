#6. Define a function that can receive two integral numbers in string form and compute their sum and print it in the console.

num1 = "1000"
num2 = "3400"
def calculate (a,b):
    result = int(a) + int(b)
    return result

sum = calculate(num1, num2)
print(sum)


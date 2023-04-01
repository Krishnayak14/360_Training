#Task2.2
Select_operation = int(input(print("Enter any numbers between 1-5")))
num1, num2, num3, num4 = 0, 0, 0, 0
if Select_operation < 5:
    num1 = int(input(print("Enter numbers")))
    num2 = int(input(print("Enter numbers")))
if Select_operation == 5:
    num1 = int(input(print("Enter numbers")))
    num2 = int(input(print("Enter numbers")))
    num3 = int(input(print("Enter numbers")))
    num4 = int(input(print("Enter numbers")))

def operators(Select_operation, num1, num2, num3, num4):
    result = None
    if Select_operation == 1:
        result = num1 + num2
    if Select_operation == 2:
        result = num1 - num2
    if Select_operation == 3:
        result = num1 * num2
    if Select_operation == 4:
        result = num1 / num2
    if Select_operation == 5:
        result = (num1 + num2 + num3 + num4) / 4

    if result < 0:
        print("NEGATIVE")
    return result

print(operators(Select_operation, num1, num2, num3, num4))
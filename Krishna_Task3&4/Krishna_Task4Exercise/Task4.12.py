#12. Write a function to compute 5/0 and use try/except to catch the exceptions

def divide():
    try:
        result = 5 / 0
    except ZeroDivisionError:
        print("Error: division")
    else:
        print("The result is:", result)

divide()

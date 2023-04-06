# 16. What is the output of the following codes:
# (i)
def foo():
    try:
     return 1
    finally:
        return 2
k = foo()
print(k)
It give 2 as an output

#(ii)
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')
a()

#It gives NameError : As we haven't defined f anywhere in the entire code
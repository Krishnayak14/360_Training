#Task 2.7

#Write a program that prints all the numbers from 0 to 6 except 3 and 6.  Expected output: 0 1 2 4 5 Note: Use ‘continue’ statement

numbers = [0,1,2,3,4,5,6]
for i in numbers:
    if i % 3 == 0:
        continue
    print(i)

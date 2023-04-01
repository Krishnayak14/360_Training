#Task 2.8

#Write a program that accepts a string as an input from the user and calculate the number of digits and letters.

num_of_char= 0
num_of_digit=0
user_input = input("Enter something!!\n")
for i in user_input:
    if i.isdigit() == True:
        num_of_digit = num_of_digit + 1

    if i.isalpha() == True:
        num_of_char = num_of_char + 1
print("Total num_of_digit:" , num_of_digit)
print("Total num_of_char:", num_of_char)

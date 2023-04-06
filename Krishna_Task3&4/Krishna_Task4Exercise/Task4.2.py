#2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
# Sample input: “abcSdefPghijQkl”
# Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

string = "abcSdefPghijQkl"
count_lower = 0
count_upper = 0
for i in string:
    if(i.islower()):
            count_lower=count_lower+1
    elif(i.isupper()):
            count_upper=count_upper+1

print("No. of Lowercase characters:", count_lower)
print("No. of Uppercase characaters:", count_upper)

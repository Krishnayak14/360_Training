#5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

list = [11,22,33,44,55,66,77,88,99,100]

new_list = []
for i in list:
    if i % 2 !=0:
        new_list.append(i)
print(new_list)
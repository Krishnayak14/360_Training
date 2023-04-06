#4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence
# after sorting them alphabetically.

string=input("Enter the hyphen-separated sequence of words: ")
l=string.split('-')
l.sort()
print('-'.join(l))
#Task2.9
#Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.

while True:
    number = int(input("Guess the lucky number \n"))
    if number == 5:
        print("Great!!! You have guessed the correct number")
        break
    else:
        answer =  input("Do you want to guess it again? Yes or No \n")
        if answer == "No":
            break

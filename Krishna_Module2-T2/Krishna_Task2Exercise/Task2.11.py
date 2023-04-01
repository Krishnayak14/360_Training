#2.11.  In the previous question, insert break after the “Good guess!” print statement. break will terminate the while loop so that users do not have to continue guessing after they found the number. If the user
#does not guess the number at all, print “Sorry but that was not very successful”


while True:
    number = int(input("Guess the lucky number \n"))
    if number == 5:
        print("Good guess")
        break

    else:
        print("Sorry but that was not very successful")
        break

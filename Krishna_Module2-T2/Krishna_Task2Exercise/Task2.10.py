#2.10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter.

counter = 0
while counter <= 5:
    number = int(input("Guess the lucky number \n"))
    if number == 5:
        print("Good guess")
        counter = counter + 1
        break

    else:
        print("Try again")
        counter = counter + 1

    if counter == 5:
        print("Game Over!!!!!")
        break

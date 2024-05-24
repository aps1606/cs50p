import random

level = input("Level: ")

while True:

    try:
        if int(level) > 0:
            break
        else:
            level = input("Level: ")
    except ValueError:
        level = input("Level: ")


ans = random.randint(1,int(level))
usrguess = input("Guess: ")

while True:

    try:
        if int(usrguess) == ans:
            print("Just right!")
            break

        elif int(usrguess) < 1:
            usrguess = input("Guess: ")

        elif int(usrguess) > ans:
            print("Too large!")
            usrguess = input("Guess: ")

        else: 
            print("Too low!")
            usrguess = input("Guess: ")
    
    except ValueError:
         usrguess = input("Guess: ")
import random

def main():

    # get level from 1 to 3
    level = get_level() 

    # generate questions and return final score
    score = generate_integer(level)
    
    # print out final score
    print("Your score is " + str(score) + " out of 10")


def get_level():

    level = input("Level: ")

    while True:
        try:
            if 0 < int(level) < 4:
                break
            else:
                level = level = input("Level: ")
        except ValueError:
            level = level = input("Level: ")

    return(int(level))
    
    
def generate_integer(digits):

    s = 0
    
    for i in range(10):

    # problems with 1, 2 or 3 digits generates x and y values accordingly
        if digits == 1:
            x = random.randrange(1, 9)
            y = random.randrange(1, 9)
            t = questions(x,y)
            s = s + t

        elif digits == 2:
            x = random.randrange(10, 99)
            y = random.randrange(10, 99)
            t = questions(x,y)
            s = s + t

        else:
            x = random.randrange(100, 999)
            y = random.randrange(100, 999)
            t = questions(x,y)
            s = s + t

    return s


def questions(x,y):
    q = str(x) + " + " + str(y) + " = "

    for i in range(3):
        s = 0
        ans = input(q)
        try:
            if x + y != int(ans):
                print("EEE")
            else:
                s = 1 # when answer is correct return 1
                break
        except ValueError:
            print("EEE")                        

        # if loop is still running on 3rd iteration (i.e., not correctly answered yet), print the answer
        if i == 2:
            print(q + str(x + y))
    
    return s

main()


'''
Pseudo


get_level():
    ask for level between 1 to 3 - if not valid input keep prompting
    now call generate_integer() - passing it appropriate level for number of digits

    
generate_intger():
    s = 0
    if level = 1:
        for i is 1 to 10:
            generate x
            generate y
            problems(x,y) - pass x and y to new function that prompts the user for the question
            problems(x,y) runs only once each time
            s = problems(x,y) - returns 1 if the answer is correct, returns 0 if the answer is wrong
            s = s + 1

            

    print s
    

    










'''
from pyfiglet import Figlet
import os
import random

# Figlet() function (from pyfiglet library) returning a Figlet object which is now stored in the variable figlet
figlet = Figlet()  

# getFonts() method run on the figlet object above to return a "list" of font names which is now stored in variable fontlist
fontlist = figlet.getFonts() 

def main():

    try:
        # code is required to check that user is inputting correct fontname and the "-f or --font" tags
        if os.sys.argv[1] == "-f" or os.sys.argv[1] == "--font": 
            try:
                fontlist.index(os.sys.argv[2])
                figgy(os.sys.argv[2])

            except ValueError:
                os.sys.exit("2 arguments required in the correct format: \n1) \"-f or --font\" and \n2) an available figlet font. \nOptionally use no command line arguments at all.")

        else: 
            os.sys.exit("2 arguments required in the correct format: \n1) \"-f or --font\" and \n2) an available figlet font. \nOptionally use no command line arguments at all.")

    except IndexError:
        figgy(random.choice(fontlist))


def figgy(x):
    usrinput = input("Input: ")
    figlet.setFont(font=x)
    print("\nOutput: \n\n" + figlet.renderText(usrinput))

main()


'''
Code:
1. run code with argv (either none or 2)
2. prompt for input
3. produce output based on argv


Notes:

if argv[1] is "-f" or "--font":
    if (fontlist.index contains argv[2]):

        > run figgy() with fontname argument
    
    except if not fontname not found
        
        > error msg
    
    
else:
    > run figgy() with random fontname

else:
    > sys.exit: "Please enter either 2 arguments in the correct format or none at all."



figgy() function:

Prompt for input

if argv = 0:
    print figgied output of the input - choose random figlet font when figgying the input

else:
    print figgied output of the input - choose figlet font specified by argv[2] when figgying the input

    


'''





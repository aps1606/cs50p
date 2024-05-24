import os
import inflect

p = inflect.engine()

namelist = []

while True:
    try:
        name = input("Name: ")
        namelist.append(name)
    
    except EOFError:

        print("\n")
        jointlist = p.join(namelist)
        print("Adieu, adieu, to " + jointlist)
        os.sys.exit()

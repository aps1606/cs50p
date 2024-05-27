import re
import sys

def main():
    
    try:
        print(convert_wrong(input("Hours: ")))


    except ValueError:
        sys.exit("Please input the time in the correct format")


def convert_wrong(s):

    if matches := re.search(r"([0-9]):*([0-9]{0,2}) ([A-Z]{2}) to ([0-9]{1,2}):*([0-9]{0,2}) ([A-Z]{2})",s):
        a = matches.group(1) # hours in the first section 
        b = matches.group(2) # minutes of the first section   
        c = matches.group(3) # AM or PM
        d = matches.group(4) # hours in the second section
        e = matches.group(5) # minutes of the second section        
        f = matches.group(6) # AM or PM

        # convert the first section from 12 hour to 24 hour
        if c == "PM":
            if int(a) < 12:
                a = str(int(a) + 12)
            elif int(a) == 12:
                a = "00"
        elif c == "AM":
            if int(a) == 12:
                a = "00" 

        # convert the second section from 12 hour to 24 hour
        if f == "PM":
            if int(d) < 12:
                d = str(int(d) + 12)
            elif int(d) == 12:
                d = "00"
        elif f == "AM":
            if int(d) == 12:
                d = "00" 

        if b == "":
            b = 0
            
        if e == "":
            e = 0
        
        if int(b) > 59 or int(e) > 59:
            raise ValueError

        return f"{int(a):02}" + ":" + " to " + f"{int(d):02}" + ":"   

    else: 
        raise ValueError
...

if __name__ == "__main__":
    main()




'''
convert from 12 hour to 24 hour:
    Inputs to Convert()
    - 9:00 AM to 5:00 PM OR
    - 9 AM to 5 PM

    return:
    - 9:00 to 17:00

Input validation (input to convert()): - RAISE ValueError
    - if not in format specified above
    - minutes <= 60
    - asddsa

Steps to convert:
    - Add 12 to hours section, except if 12 then make is 00


TESTING:
    - check that the output minutes < 60


'''
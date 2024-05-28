from datetime import date
import sys
import re
import inflect


def main():
    
    try:
        print(minutes(input("Date of birth: ")) + " minutes")
    
    except (TypeError, ValueError):
        sys.exit("Invalid date. Enter date of birth in YYYY-MM-DD format")

def minutes(dob):
    
    if matches := re.search(r"([0-9]{4})-([0-9]{2})-([0-9]{2})",dob):
        dobyear = int(matches.group(1))
        dobmonth = int(matches.group(2))
        dobdate = int(matches.group(3))
        
        try:
            minutes = int((date.today() - date(dobyear,dobmonth,dobdate)).total_seconds()/60)
        except ValueError:
            raise

        # code to convert the above minutes variable to words
        p = inflect.engine()

        return p.number_to_words(minutes)
    

if __name__ == "__main__":
    main()




'''
Psuedo/notes

- input validation in minutes() function
    - get DOB in integer form

    
- create a date object with date(dobyear, dobmonth, dobdate)
- run the @classemethod date.today() to get today's date
- subtract the above 2 using the overloaded operator "-" to get a timedelta object
- the timedelta object has an instance method that returns the number of seconds contained in the duration
- divide the number of second by 60 to get the number of minutes




'''
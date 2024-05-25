import sys
import requests
from pprint import pprint

def main():

    try:
        if float(sys.argv[1]) and len(sys.argv) < 3:
            #return btc price from getprice() - store to variable. MUltiply with argv and display the result
            price = getprice() * float(sys.argv[1])
            print(f"${price:,.4f}") 

        if len(sys.argv) > 2:
            sys.exit("Too many arguments. Only enter a number.")

    except ValueError:
        sys.exit("Command-line argument is not a number.")

    except IndexError:
        sys.exit("Missing command-line argument.")


def getprice():
    try:
        # retrieves a json object provided by the API and converts this to a python dictionary
        o = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        
        return float(o["bpi"]["USD"]["rate"].replace(",","")) # return btc price

    except requests.RequestException:
        sys.exit("Request failed")


main()

'''
Pseudo

command line argument to get number of bitcoin:
    - should sys.exit if text is typed
    - should supprt float (Value error)
    - should have argument (IndexError)


get the api file, convert to dict:
    - obtain bitcoin price from dict using the correct key and store to variable
    - multiply argv[1] with price and display result


    

    
    

'''
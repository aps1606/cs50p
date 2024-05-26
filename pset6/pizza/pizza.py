import sys
from tabulate import tabulate
import csv
from pprint import pprint

# command-line argument - exactly one required has to end in .py

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

elif sys.argv[1].rstrip()[-4:] != ".csv":
    sys.exit("Not a CSV file")

filename = sys.argv[1]

pizza = []

# open file, add data to dictreader object, add each row in the dictreader object to a new list to get a list of dictionaries

try:
    with open(filename, "r") as file:
        dreader = csv.DictReader(file)
        for row in dreader:
            pizza.append(row)

except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(pizza, headers = "keys",tablefmt = "grid"))

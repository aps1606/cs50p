import sys
import csv
import pprint

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

elif sys.argv[1].rstrip()[-4:] != ".csv":
    sys.exit("Not a CSV file")

inputfile = sys.argv[1]
outputfile = sys.argv[2]

students = []

try:

    with open(inputfile) as file:

        dreader = csv.DictReader(file)
        for row in dreader:
            students.append(row)

except FileNotFoundError:
    sys.exit("Could not read " + inputfile)

students2 = []

for student in students:
    last, first = student["name"].split(",")    

    #reorderng the keys and adding to a new list
    student2 = {
        "first": first.strip(),
        "last": last.strip(),
        "house": student["house"]
    }

    students2.append(student2)

with open(outputfile, "a") as file:
    
    dwriter = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    dwriter.writeheader()

    for student in students2:
        dwriter.writerow(student)





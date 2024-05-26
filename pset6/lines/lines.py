import sys
from pprint import pprint


# check command line arguments 

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

elif sys.argv[1].rstrip()[-3:] != ".py":
    sys.exit("Not a Python file")


filename = sys.argv[1]
lines = []

try:
    with open(filename, "r") as file:
        for i in file:
            i = i.replace(" ","") #strip blanks from left and right in all the lines in the file
            lines.append(i)

except FileNotFoundError:
    sys.exit("File does not exist")


# remove lines that start with # and blanks lines
for i in lines[::-1]:
    if i.startswith("#") or i.startswith("\n"):
        lines.remove(i)


# below section is for identifying any docstrings all across the document and deleting all text that appears between these docstrings

# creating a docindex list that stores the start and ending index of docstrings appearing in the document being checked

docindex = [] 

r = 0
for i in lines:
    if i.find("\'\'\'") != -1:
        docindex.append(r)
    r = r + 1

for i in range(1,len(docindex),2):
    docindex[i] = docindex[i] + 1

# code to delete all slices in between every "pair" of items in the docindex list 

a = len(docindex) - 2
b = len(docindex) - 1

if len(docindex) != 0:
    while True:
        try:
            for i in range(0,int(len(docindex)/2)):
                del lines[docindex[a]:docindex[b]]
                a = a - 2
                b = b - 2
        except IndexError:
            break

pprint(lines)
print(len(lines))

# print(docindex, end = "\n")
# print(lines[8:10], end = "\n")
# print(lines[10:12], end = "\n")


'''
Psuedo/notes


> expect  command line argument which should be 
    - exactly one string
    - name of a python file OR path of a python file
    - if not sys.exit


> Create blank list
> use "with" open to open up this file
> read the lines in the file and add them to the blank list (each line will be a separate item of that list)
    - use a for loop

> tidy the list up to remove
    - lines that start with #
    - or whitespace and then #
    - blank lines
    - docstrings
        - if sentence begins with "'
        - all linees in between the ""' and ""'
            - i need the deleted rows to be lines[]
        


> count the length of the list  


'''
import re
import sys


def main():
    print(count_wrong(input("Text: ")))


def count_wrong(s):
    matches = re.findall(r".* um .*",s) # replace the regex with " um " - for the function to only erroneouosly pick up "um"s with a space in lead and trailing it
    r = 0
    for i in matches:
        if i == "um":
            r = r+1  
    return r

if __name__ == "__main__":
    main()




'''
Pseudo/notes

use re.findall() functiono to count the number of times "um" appears as a standalone word and not as part of a bigger word



'''
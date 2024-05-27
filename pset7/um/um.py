import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\b\w*um\w*\b",s)
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
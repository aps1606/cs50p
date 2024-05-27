import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    
    if matches := re.search(r"([0-9]+\.[0-9+]+\.[0-9]+\.[0-9+]+)$",ip):
        a,b,c,d = matches.group(1).split(".")
        if 0 <= int(a) <= 255 and 0 <= int(b) <= 255 and 0 <= int(c) <= 255 and 0 <= int(d) <= 255:
            return True
        else:
            return False

    else:
        return False

if __name__ == "__main__":
    main()
import re
import sys

def main():
    print(validate_wrong(input("IPv4 Address: ")))

def validate_wrong(ip):
    
    if matches := re.search(r"([0-9]+\.[0-9+]+\.[0-9]+\.[0-9A-Z]+)$",ip):
        a,b,c,d = matches.group(1).split(".")
        if 0 <= int(a) <= 255:
            return True
        else:
            return False

    else:
        return False

if __name__ == "__main__":
    main()
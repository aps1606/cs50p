def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[0:2].isalpha() and s.isalnum() and len(s) > 1 and len(s) < 7: # code to check points 1, 2 and 3 below
        i = 2
        for c in s[i:]:
                if c.isnumeric():
                    if c == "0": # and i != len(s) - include this snippet in this line with "0" allowed as the last character of the number plate
                        return False # if the first number noted in the string is a 0, return Invalid
                    else:
                        for r in s[i:]: # If the first number is not zero, check subsequent characters for any alphabets
                            if r.isalpha():
                                return False # If any alphabets noted subsequent to the first number, return invalid
                    return True
                i = i + 1
        return True
    else:
        return False

main()

# Conditions to meet:
# 1. Start with two letters - DONE
# 2. No periods, spaces or punctuation marks - DONE
# 3. Minimum of 2 and Maximum of 6 characters - DONE
# 4. Numbers cannot be in the middle, i.e., no letters can follow the numbers - TO DO
# First number used cannot be a zero - TO DO



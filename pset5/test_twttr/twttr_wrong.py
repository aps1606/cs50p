

def main():

    text = input("Input: ")
    output = shorten_wrong(text)
    print("Output: " + output)


# this function is incorrect as it does not remove vowels that are capitalised 
def shorten_wrong(word):
    for c in word.lower():
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            word = word.replace(c,"")

    return word

if __name__ == "__main__":
    main()
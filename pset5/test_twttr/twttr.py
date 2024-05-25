

def main():

    text = input("Input: ")
    output = shorten(text)
    print("Output: " + output)

def shorten(word):
    for c in word:
        if c.lower() == "a" or c.lower() == "e" or c.lower() == "i" or c.lower() == "o" or c.lower() == "u":
            word = word.replace(c,"")

    return word

if __name__ == "__main__":
    main()
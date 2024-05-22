text = input("Input: ")

for c in text.lower():
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        text = text.replace(c,"")

print("Output: " + text)
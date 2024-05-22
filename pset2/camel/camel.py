text = input("camelCase: ")

for c in text:
    if c == c.capitalize():
        text = text.replace(c.capitalize(),"_"+c.lower())

print(text)
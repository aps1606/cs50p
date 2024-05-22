x, y, z = input("Expression: ").strip().split(" ")

x = int(x)
z = int(z)

if y == "+":
    print(float(x+z))
elif y == "-":
    print(float(x-z))
elif y == "*":
    print(float(x*z))
elif y == "/":
    print(x/z)


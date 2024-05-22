greeting = input("Greeting: ").lower().strip()

if greeting.startswith("h"):
    if greeting.startswith("hello"):
        print("$0")
    else:
        print("$20")
else:
    print("$100")





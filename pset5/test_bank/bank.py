
def main():

    greeting = input("Greeting: ").strip()
    print("$" + str(value(greeting)))


def value(greeting):
    if greeting.lower().startswith("h"):
        if greeting.lower().startswith("hello"):
            return 0
        else:
            return 20
    else:
        return 100

if __name__ == "__main__":
    main()




def main():

    greeting = input("Greeting: ").strip()
    print("$" + str(value_wrong(greeting)))


# this is the wrong version of the value function where only if the greeting is typed in lower by the user, the function works correctly
# if the user types the first letter in uppercase the function does not work as expected
def value_wrong(greeting):
    if greeting.startswith("h"):
        if greeting.startswith("hello"):
            return 100
        else:
            return 20
    else:
        return 0

if __name__ == "__main__":
    main()



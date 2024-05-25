def main():
    plate = input("Plate: ")
    if is_valid_wrong(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid_wrong(s):
    if s.isalnum() and len(s) > 1:
        return True
    else:
        return False


if __name__ == "__main__":
    main()


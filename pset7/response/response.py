from validator_collection import is_email

if is_email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")



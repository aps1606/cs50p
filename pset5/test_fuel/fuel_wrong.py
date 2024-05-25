
def main():

    while True:
        userinput = input("Fraction: ")    
        try:
            pct = convert_wrong(userinput)
            output = gauge_wrong(pct)
            print(output)
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
                    
# function takes str in X/Y format
def convert_wrong(fraction):
    Nr, Dr = fraction.split("/")
  
    try:
        if int(Dr) == 0:
            raise ZeroDivisionError

        if int(Nr) > int(Dr) or int(Nr) < 0 or int(Dr) < 0:
            raise ValueError

        x = (Nr)/(Dr)*100 #puprposely removed code to convert to int to fail test
        return x
    
    except ValueError: # this captures cases where a string is input by the user
        raise            

def gauge_wrong(percentage):
    
    if percentage == None:
        return None
    
    if percentage <= 1:
        return("F")
    
    elif percentage >= 99 and percentage <=100:
        return("E")

    else: return str(percentage)


if __name__ == "__main__":
    main()

def main():

    while True:
        userinput = input("Fraction: ")    
        try:
            pct = convert(userinput)
            output = gauge(pct)
            print(output)
            break
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
                    
# function takes str in X/Y format
def convert(fraction):
    Nr, Dr = fraction.split("/")
  
    try:
        if int(Dr) == 0:
            raise ZeroDivisionError

        if int(Nr) > int(Dr) or int(Nr) < 0 or int(Dr) < 0:
            raise ValueError

        x = int(int(Nr)/int(Dr)*100)
        return x
    
    except ValueError: # this captures cases where a string is input by the user
        raise            

def gauge(percentage):
    
    if percentage == None:
        return None
    
    if percentage <= 1:
        return("E")
    
    elif percentage >= 99 and percentage <=100:
        return("F")

    else: return str(percentage) + "%"


if __name__ == "__main__":
    main()
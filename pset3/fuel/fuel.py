
def main():

    userinput = input("Fraction: ")

    try:
        pct = gauge(userinput)
        
        if not pct == None:
            print(pct)

    except ValueError:
        main()
    except ZeroDivisionError:
        main()

def gauge(fraction):
    Nr, Dr = fraction.split("/")
    dec = int(int(Nr)/int(Dr)*100)

    if dec <= 1:
        return("E")
    
    elif dec >= 99 and dec <=100:
        return("F")
    
    elif dec > 100:
        main()

    else: return str(dec) + "%"

main()
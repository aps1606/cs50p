
def main():

    userinput = input("Fraction: ")
    try:
        pct = gauge(userinput)
        print(pct)

    except ValueError:
        main()
    except ZeroDivisionError:
        main()

def gauge(fraction):
    fraction = fraction.split("/")
    dec = float(fraction[0])/float(fraction[1])*100

    if dec <= 1:
        return("E")
    if dec >= 99:
        return("F")

    return f"{dec:.0f}" + "%"


main()
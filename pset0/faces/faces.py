
def main():
    
    userinput = str(input())
    userinput = convert(userinput)
    print(userinput)


def convert(a):
    a = a.replace(":)","🙂")
    a = a.replace(":(","🙁")
    return a


main()
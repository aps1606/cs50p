
def main():

    months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]

    usrinput = input("Date: ")

    if usrinput.find("/") == -1:
        month, date, year = usrinput.split(" ")
        date = date.replace("," , "")

    else:
        month, date, year = usrinput.split("/")

    if usrinput.find("/") != -1 and int(date) <= 31 and int(month) <=12:
        x = convert2(year, month, date)
        print(x)

    elif month.isalpha() and 0 <= months.index(month) <= 11 and int(date) <= 31:
        month = int(months.index(month))+1        
        x = convert1(year, month, date)
        print(x)
    else:
        main()
            
def convert1(year, month, date):

    month = f"{month:02}"
    date = f"{int(date):02}"

    return str(year) + "-" + month + "-" + str(date)

def convert2(year, month, date):

    month = f"{int(month):02}"
    date = f"{int(date):02}"
    
    return str(year) + "-" + str(month) + "-" + str(date)

main()
    



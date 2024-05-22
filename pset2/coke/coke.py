baltopay = 50


while baltopay > 0:
    print("Amount Due: " + str(baltopay))
    coin = input("Insert coin: ")
    if coin == "25" or coin == "10" or coin == "5":
        baltopay = baltopay - int(coin) 
        if baltopay < 1:
            print("Change owed: " + str(-baltopay))



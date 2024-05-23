

def main():
        
        menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }

        totalcost = 0
        while True:
            try:
                item = input("Item: ").title() # convert input into  proper case
                cost = menu.get(item,0)
                totalcost = totalcost + cost
                if cost != 0: 
                    print("Total: $" + str(totalcost))

            except EOFError:
                print("\n")
                break
          
#def total(x):

main()

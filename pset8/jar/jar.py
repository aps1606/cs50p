class Jar:
    def __init__(self, capacity=12):

# code commented out below is written to make for a better user experience. But retaining the below code makes it impossible to test this method using pytest, so commented out for now.
        # while True:
        #     try:
        #         if int(capacity) < 0:
        #             raise ValueError
        #         else:
        #             self._capacity = int(capacity)
        #             break
        #     except (ValueError, TypeError):
        #         capacity = input("Please enter a valid capacity: ")
                
        self._capacity = int(capacity)
        self._size = 0  

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, deposit):
# code commented out below is written to make for a better user experience. But retaining the below code makes it impossible to test this method using pytest, so commented out for now.
        #while True:
            # try:
                if (self.size + int(deposit)) > self.capacity:
                    raise ValueError ("Please re-enter the number of cookies to be added. The maximum capacity is 12.")
                else:
                    self._size = self.size + int(deposit)
        #       break
            # except ValueError:
            #     print("Please re-enter the number of cookies to be added. The maximum capacity is 12.")        
        
                #deposit = input("Please enter the number of cookies to be added. The maximum capacity is 12: ")

    def withdraw(self, withdraw):
# code commented out below is written to make for a better user experience. But retaining the below code makes it impossible to test this method using pytest, so commented out for now.
        # while True:
        #     try:
                if (self.size - int(withdraw)) < 0:
                    raise ValueError ("Sorry there's not enough cookies to withdraw that much.")
                else:
                    self._size = self.size - int(withdraw)
                # break
            # except ValueError:
            #     print("Sorry there's not enough cookies to withdraw that much.")
            #     withdraw = input("Please enter the number of cookies to be withdrawn: ")


    @property # only getter function set for capacity so it cannot be modified after initialisation
    def capacity(self):
        return self._capacity
    
    @property # only getter function set for size so it cannot be modified after initialisation
    def size(self):
        return self._size


def main():
    cookiejar = Jar()

    cookiejar.deposit(input("How many cookies to deposit?: "))

    cookiejar.withdraw(input("How many cookies to withdraw?: "))


    print(f"The cookie jar's capacity is {cookiejar.capacity}")

    print(cookiejar)

if __name__ == "__main__": 
    main()




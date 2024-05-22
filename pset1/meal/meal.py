def main():
    convert(input("What time is it? "))


def convert(time):
    hours,minutes = time.split(":")
    minutes = f"{float(minutes)/60:.2f}"
    newtime = float(hours) + float(minutes)

    if  6.99 < newtime < 8.01:
        print("breakfast time!")
    
    elif 11.99 < newtime < 13.01:
        print("lunch time!")
    
    elif 17.99 < newtime < 19.01:
        print("dinner time!")
 
if __name__ == "__main__":
    main()
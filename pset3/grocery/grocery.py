

glist = {}

while True:
    
    try:
        item = input()
        qty = glist.get(item,0) + 1 
        glist.update({item:qty})
        
    except EOFError:
        
        for i in sorted(glist):
            print(str(glist[i]) + " " + i.upper())
        break
import random

cash = 5000

while(True):

    print("You may bid up to five valuable paintings.\n Start with $"+ str(cash)+".Then, try to sell your collection for as much as possible")

#buying phase
    paintingsownedbyuser = 0
    store = []
    Price = []   
    for i in range(1,6):
        print("You have :" + str(cash))
        print("#" +str(i) + " item is up for sale")
        bid= input("enter the bid : " )
        while int(bid) > int(cash):
            print("Not enough money")
            bid= input("enter the bid : " )
        opponent= random.randint(150, 1150)
        print("another collector has bid: "+ str(opponent))
        if int(bid) >= int(opponent):
            print("You bought it!")
            paintingsownedbyuser = paintingsownedbyuser+1
            Price.append(str(bid))
            cash = int(cash) - int(bid)
            store.append(i)
        else:
            print("Sorry you lost it")
    print("You bought" + str(store))
    print(str(Price))
            
            
    #Selling phase
    for i in store:
        print("You may now sell your painint #"+str(i))
        offer = random.randint(1,6)
        for i in range(int(offer)):
            bid2= random.randint(500,2500)
            print("You've been offerend $"+ str(bid2)+" for this painting")
            print("You spent " + str(Price[i]))
            YorN = input("Do you accept? Y/N : ")
            if YorN == "Y":
                cash += bid2
                break
            else:
                if (i == offer-1):
                    print("Sorry that was your last chance. You have to keep that painting!")
                
    print("You started with $5000. You finished with $"+str(cash))
    again= input("Play again? Y/N : ")
    if again == "N":
        break
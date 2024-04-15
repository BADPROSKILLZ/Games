import random


#Card Check
def checkIfCard(card):
    temp=yc.count(card)
    if(temp>=1):
        return card
    else:
        print("You don't have a card with that value. ")
        card='true'
        return card

#Book Check
def checkForBook(a, b):
    for i in range(13):
        i=i+1
        i=cardFix(i)
        variable=a.count(i)
        if(variable==4):
            for j in range(4):
                a.remove(i)
            if(a==yc):
                print("You lay down a book of "+str(i)+"'s.")
                b=b+1
            elif(a==dc):
                print("The dealer lays down a book of "+str(i)+"'s.")
                b=b+1
        elif(variable!=4):
            b=b
    return b
            
            

def goFish(a):
    if(cards!=[]):
        d=random.choice(cards)
        cards.remove(d)
        d=cardFix(d)
        a.append(d)
        return d
    else:
        print("There are no more fish in the sea. ")
        
#Card Request 'Fix'
def cardFix(card):
    if(card=='1' or card==1 or card=='ace' or card=='one' or card=='Ace' or card=='One' or card=='14' or card==14 or card=='fourteen' or card=='Fourteen' or card==Ace):
        card='Ace'
        return card
    elif(card=='2' or card==2 or card=='two' or card=='Two' or card==Two):
        card='Two'
        return card
    elif(card=='3' or card==3 or card=='three' or card=='Three' or card==Three):
        card='Three'
        return card
    elif(card=='4' or card==4 or card=='four' or card=='Four' or card==Four):
        card='Four'
        return card
    elif(card=='5' or card==5 or card=='five' or card=='Five' or card==Five):
        card='Five'
        return card
    elif(card=='6' or card==6 or card=='six' or card=='Six' or card==Six):
        card='Six'
        return card
    elif(card=='7' or card==7 or card=='seven' or card=='Seven' or card==Seven):
        card='Seven'
        return card
    elif(card=='8' or card==8 or card=='eight' or card=='Eight' or card==Eight):
        card='Eight'
        return card
    elif(card=='9' or card==9 or card=='nine' or card=='Nine' or card==Nine):
        card='Nine'
        return card
    elif(card=='10' or card==10 or card=='ten' or card=='Ten' or card==Ten):
        card='Ten'
        return card
    elif(card=='11' or card==11 or card=='jack' or card==11 or card=='Eleven' or card=='Jack' or card=='eleven' or card==Jack):
        card='Jack'
        return card
    elif(card=='12' or card==12 or card=='queen' or card==12 or card=='Queen' or card=='twelve' or card=='Twelve' or card==Queen):
        card='Queen'
        return card
    elif(card=='13' or card==13 or card=='king' or card==13 or card=='King' or card=='thirteen' or card=='Thirteen' or card==King):
        card='King'
        return card
    else:
        print("Request is invalid. Try again.\n")
        card=input("What card would you like to ask for? ")
        return cardFix(card)
#Shuffle Function
def shuffle(a):
    for i in range(len(a)):
        s=random.randint(0, 51)
        temp=a[i]
        a[i]=a[s]
        a[s]=temp

#Deal Function
def deal(a):
    for i in range(7):
        d=random.choice(a)
        a.remove(d)
        if(d==1):
            d="Ace"
        elif(d==2):
            d="Two"
        elif(d==3):
            d="Three"
        elif(d==4):
            d="Four"
        elif(d==5):
            d="Five"
        elif(d==6):
            d="Six"
        elif(d==7):
            d="Seven"
        elif(d==8):
            d="Eight"
        elif(d==9):
            d="Nine"
        elif(d==10):
            d="Ten"
        elif(d==11):
            d="Jack"
        elif(d==12):
            d="Queen"
        elif(d==13):
            d="King"
        print("You get a "+str(d))
        yc.append(d)
    for i in range(7):
        d=random.choice(a)
        a.remove(d)
        if(d==1):
            d="Ace"
        elif(d==2):
            d="Two"
        elif(d==3):
            d="Three"
        elif(d==4):
            d="Four"
        elif(d==5):
            d="Five"
        elif(d==6):
            d="Six"
        elif(d==7):
            d="Seven"
        elif(d==8):
            d="Eight"
        elif(d==9):
            d="Nine"
        elif(d==10):
            d="Ten"
        elif(d==11):
            d="Jack"
        elif(d==12):
            d="Queen"
        elif(d==13):
            d="King"
        dc.append(d)
    print("The dealer gets seven unknown cards.")

def checkDFor(a, card):
    global l
    l=a.count(card)
    for i in range(l):
        a.remove(card)
        yc.append(card)
                
def checkPFor(a, card):
    global x
    x=a.count(card)
    for i in range(x):
        a.remove(card)
        dc.append(card)
            
def askDFor(card):
    checkDFor(dc, card)
    print("\nYou asked for "+str(card)+"'s.")
    if(l>0):
        print("You got "+str(l)+" "+str(card)+"(s).")
    else:
        if(cards!=[]):
            u=goFish(yc)
            cardFix(u)
            if(u=='Eight' or u=='Ace'):
                print('The dealer says "Go Fish!". You draw an '+str(u)+".")
            else:
                print('The dealer says "Go Fish!". You draw a '+str(u)+".")
        else:
            goFish(yc)
    print("Your hand is: ", end="")
    print(yc)
    
def askPFor(card):
    checkPFor(yc, card)
    print("\nThe dealer asked for "+str(card)+"'s.")
    if(x>0):
        print("The dealer got "+str(x)+" "+str(card)+"(s).")
    else:
        if(cards!=[]):
            goFish(dc)
            print('You say "Go Fish!". The dealer draws a card.')
        else:
            goFish(dc)    
    print("Your hand is: ", end="")
    print(yc)

pa=100
for t in range(pa):    
    #Decklaration
    cards=[]
    #Your Cards
    yc=[]
    #Dealer Cards
    dc=[]
    #Game Status
    game_status='Playing'
    #Player Books
    pb=0
    #Dealer Books
    db=0
    
    Jack=11
    Queen=12
    King=13
    Ace=1
    Two=2
    Three=3
    Four=4
    Five=5
    Six=6
    Seven=7
    Eight=8
    Nine=9
    Ten=10
    
    for i in range(4):
        cards.append(Ace)
        cards.append(Two)
        cards.append(Three)
        cards.append(Four)
        cards.append(Five)
        cards.append(Six)
        cards.append(Seven)
        cards.append(Eight)
        cards.append(Nine)
        cards.append(Ten)
        cards.append(Jack)
        cards.append(Queen)
        cards.append(King)
    
    print("We're going to play Go Fish.")
    shuffle(cards)
    deal(cards)
    print("It is your turn.")
    #Gameplay 
    while(game_status!='ended'):
        if(yc==[] and cards!=[]):
            nTemp=random.choice(cards)
            cards.remove(nTemp)
            nTemp=cardFix(nTemp)
            yc.append(nTemp)
            print("You drew a "+nTemp+".")
            print("Your hand is: ", end="")
            print(yc)
            #Player Request
            cq=input("What card would you like to ask for? ")
            cq=checkIfCard(cardFix(cq))
            while(cq=='true'):
                cq=checkIfCard(cardFix(cq))
            askDFor(cardFix(cq))
            pb=checkForBook(yc, pb)
            print("Player Books: "+str(pb)+".")
        elif(yc!=[]):
            #Player Request
            cq=input("What card would you like to ask for? ")
            cq=checkIfCard(cardFix(cq))
            while(cq=='true'):
                cq=checkIfCard(cardFix(cq))
            askDFor(cardFix(cq))
            pb=checkForBook(yc, pb)
            print("Player Books: "+str(pb)+".")
        else:
            print("There are no more fish in the sea.")
        if(cards==[] and yc==[] and dc==[]):
            game_status=='ended'
        if(dc==[] and cards!=[]):
            nntemp=random.choice(cards)
            cards.remove(nntemp)
            nntemp=cardFix(nntemp)
            dc.append(nntemp)
            #Dealer Request
            dq=random.choice(dc)
            askPFor(cardFix(dq))
            db=checkForBook(dc, db)
            print("Dealer Books: "+str(db))
            print("\n")
        elif(dc!=[]):
            #Dealer Request
            dq=random.choice(dc)
            askPFor(cardFix(dq))
            db=checkForBook(dc, db)
            print("Dealer Books: "+str(db))
            print("\n")
        else:
            print("There are no more fish in the sea.")
        if(cards==[] and yc==[] and dc==[]):
            game_status='ended'
    
    if(pb>db):
        print("You won! You had "+str(pb)+" books and the dealer had "+str(db)+" books.")
    elif(db>pb):
        print("The dealer won. You had "+str(pb)+" books and the dealer had "+str(db)+" books.")
    else:
        print("It's a tie! You had "+str(pb)+" books and the dealer had "+str(db)+" books.")
    paq=input("Do you want to play again? ")
    if(paq=='Yes' or paq=='yes' or paq=='y' or paq=='Y'):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        pa=pa
    else:
        exit()
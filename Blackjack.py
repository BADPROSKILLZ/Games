import random

#Article Function (a or an)
def articleChoice(card):
    match card:
        case "Ace":
            articleType = "an"
        case 8:
            articleType = "an"
        case _:
            articleType = "a"
    return articleType

#Print Cards
def printCards(recipient, cards):
    print(recipient, end="")
    for i in range(len(cards)):
        if(i == len(cards)-1 and len(cards) == 2):
            print(" and "+articleChoice(cards[i])+" "+str(cards[i])+".")
        elif(i == len(cards)-1):
            print("and "+articleChoice(cards[i])+" "+str(cards[i])+".")
        elif(i == 0):
            print(articleChoice(cards[i])+" "+str(cards[i]), end="")
        elif(i == len(cards)-2):
            print(", "+articleChoice(cards[i])+" "+str(cards[i]), end=" ")
        else:
            print(", "+articleChoice(cards[i])+" "+str(cards[i]), end="")
   
#Print Last Dealt Card
def dealt(card):
    print(articleChoice(card)+" "+str(card)+".\n")

#Ace Check
def aceCheck(points, aceList):
    for i in range(len(aceList)-1):
        if(aceList[i] == "Ace" and points>21 and aceList[i+1]==11):
            points-=10
            aceList[i+1]=1
    return points
    
#Shuffle Function
def shuffle(a):
    for i in range(len(a)):
        s=random.randint(0, 311)
        temp=a[i]
        a[i]=a[s]
        a[s]=temp

#Hit Function
def hit(Points, aceList):
    #Deal A Card
    match deck[0]: 
        case "Jack":
            Points+=10
            aceList.append("Jack")
        case "jack":
            Points+=10
            aceList.append("Jack")
        case "Queen":
            Points+=10
            aceList.append("Queen")
        case "queen":
            Points+=10
            aceList.append("Queen")
        case "King":
            Points+=10
            aceList.append("King")
        case "king":
            Points+=10
            aceList.append("King")
        case "Ace":
            if((Points+11)>21):
                Points+=1
                aceList.append("Ace")
                aceList.append(1)
            else:
                Points+=11
                aceList.append("Ace")
                aceList.append(11)
        case "ace":
            if((Points+11)>21):
                Points+=1
                aceList.append("Ace")
                aceList.append(1)
            else:
                Points+=11
                aceList.append("Ace")
                aceList.append(11)
        case _:
            Points+=deck[0]
            aceList.append(deck[0])
    card=deck[0]
    deck.pop(0)
    return Points, card

#Deal Function
def deal():
    #Variable Declaration 
    playerPoints = 0
    playerCards = []
    dealerPoints = 0
    dealerCards = []
    #Player First Card
    playerPoints, playerFirstCard = hit(playerPoints, playerAceList)
    playerCards = [playerFirstCard]
    print("You were dealt ", end=""), dealt(playerFirstCard)
    #Dealer First Card
    dealerPoints, dealerFirstCard = hit(dealerPoints, dealerAceList)
    dealerCards = [dealerFirstCard]
    print("The dealer was dealt ", end=""), dealt(dealerFirstCard)
    #Player Second Card
    playerPoints, playerSecondCard = hit(playerPoints, playerAceList)
    playerCards.append(playerSecondCard)
    print("You were dealt ", end=""), dealt(playerSecondCard)
    #Dealer Second Card
    dealerPoints, dealerSecondCard = hit(dealerPoints, dealerAceList)
    dealerCards.append(dealerSecondCard)
    print("The dealer was dealt an unknown card. \n")
    return playerPoints, playerCards, dealerPoints, dealerCards

#Current Turn
def turn(currentPlayer, Points, AceList, Cards):
    if(currentPlayer == "Player"):
        while(Points <= 21):
            #Blackjack Check
            if(Points == 21):
                print("You have Blackjack!\n")
                break
            else:
                #Player Question
                Answer = input("Do you want to hit? ")
                Answer = Answer.upper()
                if(Answer == "YES" or Answer == "Y"):
                    #Hit
                    CardsAndPoints= hit(Points, AceList)
                    Points = CardsAndPoints[0]
                    Points = aceCheck(Points, AceList)
                    newCard = CardsAndPoints[1]
                    Cards.append(newCard)
                    print("You were dealt "+articleChoice(newCard)+" "+str(newCard)+". Your point total is "+str(Points)+".", end=" "), printCards("You now have ", Cards)
                    if(Points > 21):
                        print("You went bust! \n")
                        break
                    else:
                        print("")
                elif(Answer == "NO" or Answer == "N"):
                    #Stand
                    print("You stood. Your point total is "+str(Points)+".\n")
                    break
                else:
                    print("Invalid input. Please answer yes or no.\n")
        return Points
    elif(currentPlayer == "Dealer"):
        while(Points <= 21):
            #Blackjack Check
            if(Points == 21):
                print("The dealer has Blackjack!\n")
                break
            else:
                #Dealer Decision
                if(Points < 17):
                    #Hit
                    CardsAndPoints= hit(Points, AceList)
                    Points = CardsAndPoints[0]
                    Points = aceCheck(Points, AceList)
                    newCard = CardsAndPoints[1]
                    Cards.append(newCard)
                    print("The dealer dealt themselves "+articleChoice(newCard)+" "+str(newCard)+". Their point total is "+str(Points)+".", end=" "), printCards("The dealer now has ", Cards)
                    if(Points>21):
                        print("The dealer went bust! \n")
                        break
                    else:
                        print("")
                elif(Points >= 17):
                    #Stand
                    print("The dealer stood. Their point total is "+str(Points)+".\n")
                    break
        return Points
    elif(currentPlayer == "First Hand"):
        while(Points <= 21):
            #Blackjack Check
            if(Points == 21):
                print("Your first hand has Blackjack!\n")
                break
            else:
                #Player Question
                Answer = input("Do you want to hit on your first hand? ")
                Answer = Answer.upper()
                if(Answer == "YES" or Answer == "Y"):
                    #Hit
                    CardsAndPoints= hit(Points, AceList)
                    Points = CardsAndPoints[0]
                    Points = aceCheck(Points, AceList)
                    newCard = CardsAndPoints[1]
                    Cards.append(newCard)
                    print("Your first hand was dealt "+articleChoice(newCard)+" "+str(newCard)+". It's point total is "+str(Points)+".", end=" "), printCards("Your first hand now has ", Cards)
                    if(Points > 21):
                        print("Your first hand is bust! \n")
                        break
                    else:
                        print("")
                elif(Answer == "NO" or Answer == "N"):
                    #Stand
                    print("You stood on your first hand. It's point total is "+str(Points)+".\n")
                    break
                else:
                    print("Invalid input. Please answer yes or no. ")
        return Points
    elif(currentPlayer == "Second Hand"):
        while(Points <= 21):
            #Blackjack Check
            if(Points == 21):
                print("Your second hand has Blackjack!\n")
                break
            else:
                #Player Question
                Answer = input("Do you want to hit on your second hand? ")
                Answer = Answer.upper()
                if(Answer == "YES" or Answer == "Y"):
                    #Hit
                    CardsAndPoints= hit(Points, AceList)
                    Points = CardsAndPoints[0]
                    Points = aceCheck(Points, AceList)
                    newCard = CardsAndPoints[1]
                    Cards.append(newCard)
                    print("Your second hand was dealt "+articleChoice(newCard)+" "+str(newCard)+". It's point total is "+str(Points)+".", end=" "), printCards("Your second hand now has ", Cards)
                    if(Points > 21):
                        print("Your second hand is bust! \n")
                        break
                    else:
                        print("")
                elif(Answer == "NO" or Answer == "N"):
                    #Stand
                    print("You stood on your second hand. It's point total is "+str(Points)+".\n")
                    break
                else:
                    print("Invalid input. Please answer yes or no. ")
        return Points
        
#Check Value of a Card
def valueCheck(card):
    match card:
        case "Jack":
            value = 10
        case "Queen":
            value = 10
        case "King":
            value = 10
        case "Ace":
            value = 11
        case _:
            value = card
    return value

#Split Function
def split(cards):
    answer = ""
    while(answer != "NO" or answer != "N"):
        if(valueCheck(cards[0]) == valueCheck(cards[1])):
            answer = input("Would you like to split? ")
            answer = answer.upper()
            #Split
            if(answer == "YES" or answer == "Y"):
                print("You split your cards into two hands. \n")
                #First Hand
                FirstHand = [cards[0]]
                FirstHandPoints = valueCheck(cards[0])
                FirstHandAceList = []
                if(cards[0] == "Ace"):
                    FirstHandAceList.append(cards[0]), FirstHandAceList.append(11)
                else:
                    FirstHandAceList.append(cards[0])
                FirstHandCardsAndPoints = hit(FirstHandPoints, FirstHandAceList)
                FirstHandPoints = FirstHandCardsAndPoints[0]
                FirstHandNewCard = FirstHandCardsAndPoints[1]
                FirstHand.append(FirstHandNewCard)
                print("Your first hand was dealt "+articleChoice(FirstHandNewCard)+" "+str(FirstHandNewCard)+". It's point total is "+str(FirstHandPoints)+".", end=" "), printCards("Your first hand now has ", FirstHand), print("\n")
                
                #Second Hand
                SecondHand = [cards[1]]
                SecondHandPoints = valueCheck(cards[1])
                SecondHandAceList = []
                if(cards[1] == "Ace"):
                    SecondHandAceList.append(cards[1]), SecondHandAceList.append(11)
                else:
                    SecondHandAceList.append(cards[1])
                SecondHandCardsAndPoints = hit(SecondHandPoints, SecondHandAceList)
                SecondHandPoints = SecondHandCardsAndPoints[0]
                SecondHandNewCard = SecondHandCardsAndPoints[1]
                SecondHand.append(SecondHandNewCard)
                print("Your second hand was dealt "+articleChoice(SecondHandNewCard)+" "+str(SecondHandNewCard)+". It's point total is "+str(SecondHandPoints)+".", end=" "), printCards("Your second hand now has ", SecondHand), print("\n")
                cards.clear()
                return answer, FirstHand, FirstHandPoints, FirstHandAceList, SecondHand, SecondHandPoints, SecondHandAceList
            #No Split
            elif(answer == "NO" or answer == "N"):
                print()
                answer, FirstHand, FirstHandPoints, FirstHandAceList, SecondHand, SecondHandPoints, SecondHandAceList = "NO", 0, 0, 0, 0, 0, 0
                return answer, FirstHand, FirstHandPoints, FirstHandAceList, SecondHand, SecondHandPoints, SecondHandAceList
            else:
                print("Invalid Input. Please answer yes or no.\n")
        else:
            answer, FirstHand, FirstHandPoints, FirstHandAceList, SecondHand, SecondHandPoints, SecondHandAceList = "NO", 0, 0, 0, 0, 0, 0
            return answer, FirstHand, FirstHandPoints, FirstHandAceList, SecondHand, SecondHandPoints, SecondHandAceList
#Chip System
#Betting Function
#Double Down Function

#MAIN 
#6 deck declaration
playerChips = 50
playAnswer = ""
while(playAnswer != "NO" or playAnswer != "N"):
    if(playAnswer == ""):
        playAnswer = input("Do you want to play Blackjack? ")
    else:
        playAnswer = input("Do you want to play again? ")
        for i in range(54):
            print("\r")
    playAnswer = playAnswer.upper()
    if(playAnswer == "NO" or playAnswer == "N"):
        print("*You leave the blackjack table*")
        exit()
    elif(playAnswer == "YES" or playAnswer == "Y"):
        #bet = int(input("How many chips would you like to bet? "))
        ace="Ace"
        queen="Queen"
        jack="Jack"
        king="King"
        deck=[ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]*24
        playerAceList = []
        dealerAceList = []
        shuffle(deck)
        '''print(deck, "\n")'''
        print("\nWelcome to the Blackjack table! The dealer stands on 17+\n----------------------------------------------------------\n")
        #Dealing
        playerPoints, playerCards, dealerPoints, dealerCards = deal()
        print("Your current point total is "+str(playerPoints)+".", end=" "), printCards("You now have ", playerCards), print("")
        print("The dealer's cards are "+articleChoice(dealerCards[0])+" "+str(dealerCards[0])+" and an unknown card.\n")
        #Player Turn
        splitAnswer, firstHand, firstHandPoints, firstHandAceList, secondHand, secondHandPoints, secondHandAceList = split(playerCards)
        if(splitAnswer == "YES" or splitAnswer == "Y"):
            doubleDown = input("Would you like to double down on your first hand? ")
            firstHandPoints = turn("First Hand", firstHandPoints, firstHandAceList, firstHand)
            doubleDown = input("Would you like to double down on your second hand? ")
            secondHandPoints = turn("Second Hand", secondHandPoints, secondHandAceList, secondHand)
            #Dealer Turn
            print("The dealer's unknown card is "+articleChoice(dealerCards[1])+" "+str(dealerCards[1])+".")
            dealerPoints = turn("Dealer", dealerPoints, dealerAceList, dealerCards)
            #First Hand Victor Check
            if(firstHandPoints > 21):
                print("The dealer beat your first hand!\n")
            elif(dealerPoints > 21):
                print("Your first hand beat the dealer!\n")
            elif(firstHandPoints == dealerPoints):
                print("Your first hand tied the dealer!\n")
            elif(firstHandPoints > dealerPoints):
                print("Your first hand beat the dealer!\n")
            else:
                print("The dealer beat your first hand!\n")
            
            #Second Hand Victor Check
            if(secondHandPoints > 21):
                print("The dealer beat your second hand!\n")
            elif(dealerPoints > 21):
                print("Your second hand beat the dealer!\n")
            elif(secondHandPoints == dealerPoints):
                print("Your second hand tied the dealer!\n")
            elif(secondHandPoints > dealerPoints):
                print("Your second hand beat the dealer!\n")
            else:
                print("The dealer beat your second hand!\n")
        else:
            playerPoints = turn("Player", playerPoints, playerAceList, playerCards)
            if(playerPoints > 21):
                print("The dealer won! ")
            else:
                #Dealer Turn
                print("The dealer's unknown card is "+articleChoice(dealerCards[1])+" "+str(dealerCards[1])+".")
                dealerPoints = turn("Dealer", dealerPoints, dealerAceList, dealerCards)
                #Victor Check
                if(dealerPoints > 21):
                    print("You win!")
                elif(playerPoints == dealerPoints):
                    print("You and the dealer tied!")
                elif(playerPoints > dealerPoints):
                    print("You won!")
                else:
                    print("The dealer won!")
    else:
        print("Invalid input. Please enter yes or no.\n")
        playAnswer = ""


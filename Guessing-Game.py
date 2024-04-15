#Made fall of 22

import random
e=random.randint(1, 100)
#prompt
que=input("Do you want to play a game? (Y/N) ")
c=1
#Yes
if(que=="Y" or que=="y"):
    print("Alright, we are going to play a guessing game. ")
    #Difficulty Choice
    que2=input("What difficulty would you like to play on? Easy, Medium, Hard or Extreme? ")
    #Easy
    if(que2=="Easy" or que2=="easy"):
        print("Alright. I am thinking of a whole number from 1 to 100")
        random.seed(e)
        num=random.randint(1, 100)
        guess=int(input("Enter a number between 1 and 100 "))
        while(guess!=num):
            if(guess>num):
                #Easy high
                print("Guess too high. Try again. ")
                guess=int(input("Enter a whole number from 1 to 100 "))
                c=c+1
            elif(guess<num):
                #Easy low
                print("Guess too low. Try again.")
                guess=int(input("Enter a whole number from 1 to 100 "))
                c=c+1
        #Easy correct
        if(guess==num):
            print("Correct! You got it in "+ str(c) + " tries. ")
    #Medium
    elif(que2=="Medium" or que2=="medium"):
        random.seed(e)
        num=random.randint(1, 100)
        guess=int(input("Enter a number between 1 and 100 "))
        while(guess!=num and c<15):
            if(guess>num):
                #Medium high
                print("Guess too high. Try again. ")
                guess=int(input("Enter a whole number from 1 to 100 "))
                c=c+1
            elif(guess<num):
                #Medium low
                print("Guess too low. Try again.")
                guess=int(input("Enter a whole number from 1 to 100 "))
                c=c+1
        #Medium correct
        if(guess==num):
            print("Correct! You got it in "+ str(c) + " tries. ")
        #Medium Fail
        elif(c==15 and guess!=num):
            print("Incorrect. You didn't get it. The number was " + str(num) + ".\nYou tried " + str(c) + " times. ")
    #Hard
    elif(que2=="Hard" or que2=="hard"):
        random.seed(e)
        num=random.randint(1, 100)
        guess=int(input("Enter a number between 1 and 100 "))
        while(guess!=num and c<5):
            if(guess>num):
                #Hard high
                print("Guess too high. Try again. ")
                guess=int(input("Enter a whole number from 1 to 100 "))
                c=c+1
            elif(guess<num):
                #Hard low
                print("Guess too low. Try again.")
                guess=int(input("Enter a whole number from 1 to 100 "))
                c=c+1
        #Hard correct
        if(guess==num):
            print("Correct! You got it in "+ str(c) + " tries. ")
        #Hard fail
        elif(c==5 and guess!=num):
            print("Incorrect. You didn't get it. The number was " + str(num) + ".\nYou tried " + str(c) + " times. ")
    #Extreme
    elif(que2=="Extreme" or que2=="extreme"):
        random.seed(e)
        num=random.randint(1, 1000)
        guess=int(input("Enter a number between 1 and 1000 "))
        while(guess!=num and c<10):
            if(guess>num):
                #Extreme high
                print("Guess too high. Try again. ")
                guess=int(input("Enter a whole number from 1 to 1000 "))
                c=c+1
            elif(guess<num):
                #Extreme low
                print("Guess too low. Try again.")
                guess=int(input("Enter a whole number from 1 to 1000 "))
                c=c+1
        #Extreme correct
        if(guess==num):
            print("Correct! You got it in "+ str(c) + " tries. ")
        #Extreme fail
        elif(c==10 and guess!=num):
            print("Incorrect. You didn't get it. The number was " + str(num) + ".\nYou tried " + str(c) + " times. ")
    else:
        #Invalid difficulty
        print("Invalid Input. Restart the program to try again. ")
            
        
#No
elif(que=="N" or que=="n"):
    print("Alright, goodbye. ")
else:
    #Invalid
    print("Input not valid, please try again. ")

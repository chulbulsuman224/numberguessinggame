import random
chance=5
number= random.randint(1,9)

while(chance>=0):
        guessno=int(input("Guess a number (between 1 to 9)"))  
        chance = chance-1
        if guessno == number:
                print("congratulation YOU WIN")
                break
        elif guessno<number:
                print("guess a heigher number ")
        else: 
                print("guess a lower number")

if not chance>=0:
        print("you LOSE")
        

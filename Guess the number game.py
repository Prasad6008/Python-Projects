import random

num = random.randint(1,20)


guess = int(input("Can you guess the number <=20 ? :"))

chances = 3

while num != guess:
    chances -=1 #decreasing chances
    if num > guess:
        print("You Guess is low")
    else:
        print("Your Guess is high")

    if chances != 0:
        print("Remaining Chances:",chances)
        guess = int(input("Guess again:"))
    else:
        print("YOU LOOSE 'BETTER LUCK NEXT TIME' ")
        break
else:
    print("=*=*=YOU WIN=*=*=")
        
        
    

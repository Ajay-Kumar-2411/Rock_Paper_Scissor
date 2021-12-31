# Rock, Paper, Scissor - Game

import random

your_score = 0
comp_score = 0

print("Enter the number of turns you want to play: ",end = '')
n = int(input())        

while (n>0):
    randNo = random.randint(1,3)

    # gameWin() function START 
    def gameWin(comp,you):
        if comp == you:
            return None
        elif comp == "r":
            if you == "p":
                return True
            elif you == "s":
                return False
        elif comp == "p":
            if you == "s":
                return True
            elif you == "r":
                return False
        elif comp == "s":
            if you == "r":
                return True
            elif you == "p":
                return False 
    # gameWin() function END

    if randNo == 1:
        comp = "r"
    elif randNo == 2:
        comp = "p"
    elif randNo == 3:
        comp = "s"

    you = input("Your Turn: Enter r for Rock, p for Paper or s for Scissor: ")

    result = gameWin(comp,you)
    print(f"Computer Choose {comp}")
    print(f"You Choose {you}")

    if result == None:
        print("The game is tie!")
    elif result:
        print("Congratulations ! You Win")
        your_score = your_score + 10
    else:
        print("Better Luck Next Time ! You Lose")
        comp_score = comp_score + 10

    with open("hiscore_rps.txt","r") as f:
        data = f.read()

    if data == '':
        if comp_score > your_score:
            with open("hiscore_rps.txt","w") as f:
                f.write(str(comp_score))
        else:
            with open("hiscore_rps.txt","w") as f:
                f.write(str(your_score))
            
    else:
        with open("hiscore_rps.txt","r") as f:
            score = f.read()
        if your_score > comp_score:
            if int(score) < your_score:
                with open("hiscore_rps.txt","w") as f:
                    f.write(str(your_score))
        elif your_score < comp_score:
            if int(score) < comp_score:
                with open("hiscore_rps.txt","w") as f:
                    f.write(str(comp_score))
        
    n = n-1

print(f"Your Current Score is: {your_score}")
print(f"Computer Current Score is: {comp_score}")

with open("hiscore_rps.txt","r") as f:
    hiscore = f.read()

print("High Score is: " + hiscore)
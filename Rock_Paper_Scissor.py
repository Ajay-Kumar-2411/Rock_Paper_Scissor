# Rock, Paper, Scissor - Game

import random

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
else:
    print("Better Luck Next Time ! You Lose")
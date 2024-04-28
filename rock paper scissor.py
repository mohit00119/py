#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ASUS
#
# Created:     28/04/2024
# Copyright:   (c) ASUS 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == "rock":
        if you == "scissor":
            return False
        else:
            return True
    elif comp == "paper":
        if you == "rock":
            return False
        else:
            return True
    elif comp == "scissor":
        if you == "paper":
            return False
        else:
            return True

print("comp turns: rock(r), paper(p), scissor(s)? :")
randNO = random.randint(1, 3)
if randNO == 1:
    comp = "rock"
elif randNO == 2:
    comp = "paper"
elif randNO == 3:
    comp = "scissor"

you = input("your turn: rock(r), paper(p), scissor(s)? :")
a = gamewin(comp.lower(), you.lower())
print(f"computer choose: {comp}")
print(f"you choose: {you}")

if a == None:
    print("THE GAME IS TIE!")
elif a:
    print('You win!')
else:
    print('You lose!')
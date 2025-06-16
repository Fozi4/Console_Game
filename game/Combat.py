from random import randint
from Enemies import *
from Characters import * 
attacks = ["attack", Player.ability]
combat = True
turn = randint(1,2)
guess = input("Guess a number to decide who goes first(1 or 2): ")
if turn == guess:
    print("You go first")
    your_turn = True
else:
    print("You go second")
    your_turn = False
while combat:
    if your_turn == True:
        for i in attacks:
            print(i,end=" ")
        type_of_attack = input("Choose type of attack")
        combat = False
        
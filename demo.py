import random
import os
import re
while True:
    print('Rock,Paper,Scissors--shoot!')
    print('please choose a letter: "R" or "P" or "S"')
    userchoice=input('choose your weapon:')
    print('you chose:',userchoice)
    opponent=['R','P','S']
    opponentchoice=random.choice(opponent)
    print('opponent chose:',opponentchoice)
    if opponentchoice==str.upper(userchoice):
        print('it"s a tie')
    if opponentchoice=="R" and userchoice==str.upper("P"):
        print('rock beats paper')
        print('opponent wins')
    elif opponentchoice=="R" and userchoice==str.upper("S"):
        print('scissors beats rock,you wins')
    elif opponentchoice=="P" and userchoice=="R":
        print('rock beats paper,you win')
    #elif opponentchoice==userchoice:
        #print('its a tie')
    elif opponentchoice=="P" and userchoice=="S":
        print('scissors beats paper,you wins')
    elif opponentchoice=="S" and userchoice=="R":
        print('scissors beats rocks,opponent wins')
    elif opponentchoice=="S" and userchoice=="P":
        print('scissors beats paper,opponent wins')

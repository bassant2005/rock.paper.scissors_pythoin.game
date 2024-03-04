#rock,paper,scissors
choices=["rock","paper","scissors"]
import random
computer=random.choice(choices)
again=input("start? (yes/no)...")
while again=="yes":
    player=input('''rock,paper,or scissors ?
    ''').lower()
    if player==computer:
        print("you: ",player)
        print("computer: ",computer)
        print("We tied!") 
    elif player=="rock" and computer=="paper":
        print("you: ",player)
        print("computer: ",computer)
        print("you lost :(")
    elif player=="rock" and computer=="scissors":
        print("you: ",player)
        print("computer: ",computer)
        print("you won ;)")
    elif player=="paper" and computer=="scissors":
        print("you: ",player)
        print("computer: ",computer)
        print("you lost :(")
    elif player=="paper" and computer=="rock":
        print("you: ",player)
        print("computer: ",computer)
        print("you won ;)")
    elif player=="scissors"and computer=="rock":
        print("you: ",player)
        print("computer: ",computer)
        print("you lost :(")
    elif player=="scissors" and computer=="paper":
        print("you: ",player)
        print("computer: ",computer)
        print("you won ;)")
    else:
        print("not valid choise,try again")
    again=input("again? (yes/no)...")
    if again=="no":
        print("bye! ^_^")
        break
    else:
        continue

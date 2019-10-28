from random import randint
rand_choice=randint(0,2)
play_time=3
computer_wins=0
player_wins=0
if randint=="0":
    computer="rock"
elif randint=="1":
    computer="paper"
else:
    computer="scissors"

while player_wins<play_time and computer_wins<play_time:
    player=input("enter the choice you want to play.")
    if player=="quit" or player=="q":
        break
    elif player=="rock":
        if computer=="paper":
            computer_wins+=1
            print(f"computer wins {computer_wins}")
        elif computer=="scissors":
            player_wins+=1
            print(f"player wins {player_wins}")
        else:
            print("its a tie")
    elif player=="paper":
        if computer=="rock":
            player_wins+=1
            print(f"player wins {player_wins}")
        elif computer=="scissors":
            computer_wins+=1
            print(f"computer wins {computer_wins}")
        else:
            print("its a tie")
    elif player=="scissors":
        if computer=="rock":
            computer_wins+=1
            print(f"computer wins {computer_wins}")
        elif computer=="paper":
            player_wins+=1
            print(f"player wins {player_wins}")
        else:
            print("its a tie")
    else:
        print("you have entered a wrong choice")
        break

if player_wins>computer_wins:
    print("player wins")
elif player_wins==computer_wins:
    print("its a tie")
else:
    print("computer wins")


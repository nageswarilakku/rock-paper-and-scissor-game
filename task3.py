#rock paper and scissors game 
import random
options=("rock","paper","scissors")
player=None
computer= random.choice(options)
while player not in options:
    player=input("enter a choice (rock,paper,scissors): ")

print(f"player:{player}")
print (f"computer:{computer}")
if player==computer:
    print("it is tie")
    print("you get 50 score")
elif player=="rock"and computer=="scissors":
    print("you win game!")
    print("you 70 score")
elif player=="paper" and computer=="rock":
    print("you lose game!")
    print("you get 25 score")
elif player=="scissors" and computer=="paper":
    print("you win game!")
    print("you get 100 score")
else:
    print("you lose game!")
    print("you get 0 score")
import random

def winConditionRPS():
  return True

def compareRPS(choice1, choice2):
  if choice1 == choice2:
    return 0
  elif choice1 == "rock":
    if choice2 == "scissors":
      return 1
    elif choice2 == "paper":
      return 2
  elif choice1 == "scissors":
    if choice2 == "paper":
      return 1
    elif choice2 == "rock":
      return 2
  elif choice1 == "paper":
    if choice2 == "rock":
      return 1
    elif choice2 == "scissors":
      return 2
  else:
    print ("these aren't valid RPS words! calling it a tie...")
    return 0


def RPS():
  CPUScore = 0
  PlayerScore = 0
  choices = ["rock", "paper", "scissors"]
  while CPUScore < 2 and PlayerScore < 2:
    CPU_choice = choices[random.randint(1, 3)-1]
    Player_choice = ""
    while not Player_choice in choices:
      Player_choice = input("rock, paper, scissors, shoot! what did you choose? ")
      Player_choice = Player_choice.lower()
      if not Player_choice in choices:
        print ("whoops! that's not rock, paper, or scissors!")
    print ("great, you selected " + Player_choice + " while i selected " + CPU_choice)
    winner = compareRPS(CPU_choice, Player_choice)
    if winner == 0:
      print ("this round is a tie! i guess we go again! i'll get you this time! \n")
    elif winner == 1:
      CPUScore == CPUScore + 1
      print ("L")
    elif winner == 2:
      PlayerScore = PlayerScore + 1
      print ("im bad, you win gg \n")

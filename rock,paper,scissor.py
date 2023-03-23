import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]


while True:
    user_input = input('Type Rock/Paper/Scissor or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # 0 -> rock , 1 -> paper, 2 -> scissor

    computer_pick = options[random_number]
    print("computer picked", computer_pick + '.')

    if user_input == computer_pick:
        print("you both picked the same option")

    elif user_input == "rock" and computer_pick == "scissor":
        print("You Win!!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!!")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You Win!!")
        user_wins += 1

    else:
        print("You Lost!")
        computer_wins += 1

print("you won", user_wins, "times.")
print("computer won", computer_wins, "times.")
print("\n")
print("Good Bye!")


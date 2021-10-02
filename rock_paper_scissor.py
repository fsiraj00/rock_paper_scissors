import random
draws =0
user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q to exit. ").lower() 

    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Not a valid option! Try again.")
        continue

    # rock = 0, paper = 1, scissors = 2
    random_number = random.randint(0,2)
    
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input =="rock" and computer_pick == "scissors":
        print('You won!')
        user_wins += 1
    elif user_input =="scissors" and computer_pick == "paper":
        print('You won!')
        user_wins += 1
    elif user_input =="paper" and computer_pick == "rock":
        print('You won!')
        user_wins += 1
    elif user_input == computer_pick:
        print("You drew")
        draws += 1
    else:
        print("You lost!")
        computer_wins += 1
        
print(f"You won {user_wins} times.\nComputer won {computer_wins} times. \nTotal Draws: {draws}.")
print("GGs!")
#Rock Paper Scissors

import random
user_action = input("Enter a choice {[R]ock, [P]aper, [S]cissors} : ").upper()
possible_actions=['R', 'P', 'S']
computer_action = random.choice(possible_actions)
print(f'Your choice {user_action}, computer choice {computer_action}')
if user_action == computer_action:
    print(f'Both players selected{user_action}, Its Tie :|')
elif user_action == 'R':
    if computer_action == 'S':
        print("Rock Smashes Scissors! You Win :)")
    else:
        print("Paper covers Rock! You Lose :/")
elif user_action == 'P':
    if computer_action == 'S':
        print("Scissors cuts Paper! You Lose :/")
    else:
        print("Paper covers Rock! You Win :)")
elif user_action == 'S':
    if computer_action == 'P':
        print("Scissors cuts Paper! You Win :)")
    else:
        print("Rock Smashes Scissors! You Lose :/")
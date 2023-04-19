rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice >= 3 or player_choice < 0:
    print("This is not a valid input.")
else:
    print(images[player_choice])
    robot_choice = random.randint(0, 2)
    print("Robot chose:")
    print(images[robot_choice])

    if player_choice >= 3 or player_choice < 0:
        print("This is not a valid input.")
    elif player_choice == 0 and robot_choice == 2:
        print("You win!")
    elif robot_choice == 0 and player_choice == 2:
        print("You lose!")
    elif robot_choice > player_choice:
        print("You lose!")
    elif player_choice > robot_choice:
        print("You win!")
    elif robot_choice == player_choice:
        print("Its a tie!")


import random

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
game_images = [rock, paper, scissors]

n=int(input('enter the choice  1 for rock, 2 for paper, 3 for scissors:'))
if n<=0 and n>3:
    print("invalid input")
user_choice=[] 
user_choice = game_images[n-1]
print(user_choice)
comp_choice  = random.choice(game_images)
print(comp_choice)

if  user_choice == comp_choice:
    print("its a tie")
elif  user_choice == rock and comp_choice == scissors:
    print("rock smashes scissors, you win!")
elif   user_choice == rock and comp_choice == paper:
    print("paper covers rock, you lose!")
elif   user_choice == paper and comp_choice == rock:
    print("paper covers rock, you win !")
elif   user_choice == paper and comp_choice == scissors:
    print("scissors cuts paper, you lose!")
elif   user_choice == scissors and comp_choice == rock :
    print("rock smashes scissors, you lose!")
elif   user_choice == scissors and comp_choice == rock :
    print("scissors cuts paper, you win!")

   
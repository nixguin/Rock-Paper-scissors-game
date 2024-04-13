rocks=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images=[rocks,paper,scissors]
print("Welcome to the Game of Rock, Paper, Scissors.")
choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[choose])
import random

game=random.randint(0,2)
print(f"The Computer Choose:")
print(game_images[game])

if choose>=3 or choose<=-1:
    print("Please type a valid number")
elif choose == 0 and game ==2:
    print("You guys draw")
elif game>choose:
    print("You lose")
elif game==choose:
    print("It's a draw")
elif game==0 and choose==2:
        print("You loss")
elif choose>game:
     print("You Win")

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
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
gameImages = [rock,paper,scissors]
if userInput <0 or userInput >=3:
    print("You typed an incorrect number")
else:
    print(gameImages[userInput])
    computerInput = random.randint(0,2)
    print("Computer chose:")
    print(gameImages[computerInput])

    if userInput == 0 and computerInput == 2:
        print("You win")
    elif computerInput == 0 and userInput == 2:
        print("You Lose")
    elif computerInput > userInput:
        print("You lose")
    elif userInput > computerInput:
        print("You win")
    elif userInput == computerInput:
        print("It's a tie")


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
rock_paper_scissors = [rock, paper, scissors]
player = int(input("what do you choose? type 0 for Rock, 1 for paper and 2 for scissors \n"))
print(rock_paper_scissors[player])

computer = random.randint(0, 2)
print(f"Computer chose: {rock_paper_scissors[computer]}")

if (
    (computer == 0 and player == 0) or
    (computer == 1 and player == 1) or
    (computer == 2 and player == 2)
):
    print("It's a draw!")
elif (
    (computer == 0 and player == 2) or
    (computer == 1 and player == 0) or
    (computer == 2 and player == 1)
):
    print("You lose!")
else:
    print("You win!")





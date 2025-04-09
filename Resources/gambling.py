# main.py


# from main import You

import random
# playernums = []
# bet = int(input("How much do you want to bet? "))
# You.money -= bet
# while len(playernums) != 3:
#   c = int(input("Enter a number between 1 and 20. "))
#   if c not in playernums:
#     playernums.append(c)
#   else:
#     print("You already picked that number.")
    
# numspicked = []
# for i in range(3):
#   numspicked.append(random.randint(1, 50))
# for nums in playernums:
#   if nums in numspicked:
#     print("You won!")
#     You.money += bet * 2
#     print(nums)
# print(numspicked)

def blackjack():
  bet = int(input("How much do you want to bet? "))
  # You.money -= bet
  playercards = []
  dealercards = []
  for i in range(2):
    playercards.append(random.randint(1, 11))
    dealercards.append(random.randint(1, 11))
  print(f"Your cards are {playercards} your total is {sum(playercards)}.")
  while sum(playercards) <= 21 or sum(dealercards) <= 21:
    choice = input("Do you want to hit or stay? ")
    if sum(playercards) > 21:
      print("You busted!")
      break
    if sum(dealercards) > 21:
      print("The dealer busted!")
      break
    if choice == "hit":
      playercards.append(random.randint(1, 11))
      print(f"Your cards are {playercards} your total is {sum(playercards)}.")
    elif choice == "stay":
      # dealers turn
      while sum(dealercards) < 19:
        dealercards.append(random.randint(1, 11))
      print(f"The dealer's cards are {dealercards}")
      if sum(dealercards) > sum(playercards) and sum(dealercards) <= 21:
        print(f"The dealers cards are {dealercards} and the total is {sum(dealercards)}")
        print("The dealer won!")
        break
      elif sum(dealercards) < sum(playercards) and sum(playercards) <= 21:
        print("You won!")
        # You.money += bet * 2
        break
blackjack()
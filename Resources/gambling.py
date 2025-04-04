# main.py


import random
playernums = []
for i in range(3):
  playernums.append(int(input("Enter a number between 1 and 20. ")))
numspicked = []
for i in range(3):
  numspicked.append(random.randint(1, 50))
for nums in playernums:
  if nums in numspicked:
    print("You won!")
    print(nums)
print(numspicked)
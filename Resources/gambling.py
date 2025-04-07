# main.py


import random
playernums = []
while len(playernums) != 3:
  c = int(input("Enter a number between 1 and 20. "))
  if c not in playernums:
    playernums.append(c)
  else:
    print("You already picked that number.")
    
numspicked = []
for i in range(3):
  numspicked.append(random.randint(1, 50))
for nums in playernums:
  if nums in numspicked:
    print("You won!")
    print(nums)
print(numspicked)
# graphs.py

import tkinter as tk
from classes import Graph, EventNode, AgeNode, MainMenu, EventCategory, Cat, Dog
import random
from main import Mother, Father, Sister, You, Brother
from data_structures import sponsors, sickness, boy_pet_names, girl_pet_names

G = Graph()

# -------------------------------------------------------

Activiies = MainMenu("Activiies")
for i in range(0, 30):
  AgeRoot = AgeNode(i)
  G.add_node(AgeRoot)
  Occupation = MainMenu(f"Occupation{i}")
  G.add_node(Occupation)
  Assets = MainMenu(f"Assets{i}")
  G.add_node(Assets)
  Relationships = MainMenu(f"Relationships{i}")
  G.add_node(Relationships)
  G.add_node(Activiies)
  G.add_node(AgeRoot)
  G.add_edge(AgeRoot, Occupation)
  G.add_edge(AgeRoot, Assets)
  G.add_edge(AgeRoot, Relationships)
  G.add_edge(AgeRoot, Activiies)
  
# -------------------------------------------------------

'''
dic = {
  "Message" : [
    ("Option 1", "print('Option 1')"),
    ("Option 2", "print('Option 2')")
  ]
}
'''

for node in G.agenodes:
  if node.key == 0:
    doctor = EventCategory("Doctor")
    G.add_node(doctor)
    G.add_edge(Activiies, doctor)
    dic = {
      "Which doctor do you want to go to? It costs $100 for a visit." : [
        ("Go to Dr. Larry", '''
if You.money >= 100:
  You.money -= 100
  if len(You.sickness) > 0:
    if random.randint(1, 4) == 1:
      print('Dr. Larry tried treating you but he failed')
    else:
      print(f'Dr. Larry treated you for {You.sickness.pop()}')
  else:
    print('You don't have any sickness.')
        '''),
        ("Go to Dr. Bob", '''
if You.money >= 100:
  You.money -= 100
  if len(You.sickness) > 0:
    if random.randint(1, 8) == 1:
      print('Dr. Bob tried treating you but he failed')
    else:
      print('Dr. Bob treated you')
      You.sickness.pop()
  else:
    print('You dont have any sickness.')
        '''),
        ("Im not sick!", "print('You decided that you are not sick.')")
      ]
    }
    western = EventNode("Western Medicine", dic)
    G.add_node(western)
    G.add_edge(doctor, western)
  if node.key == 4:
    pet = EventCategory("Pet")
    G.add_node(pet)
    G.add_edge(Activiies, pet)
    dic = {
      "You went to the animal shelter. It costs $175 for a cat or a dog." : [
        ("Get a boy cat", """
if You.money >= 175:
  You.money -= 175
  cat = Cat(random.choice(boy_pet_names, random.randint(0, 4), "Male", You)
  You.pets.append(cat)
else:
  print("You don't have enough money.")
        """),
        ("Get a girl cat", """
if You.money >= 175:
  You.money -= 175
  cat = Cat(random.choice(girl_pet_names, random.randint(0, 4), "Female", You)
  You.pets.append(cat)
else:
  print("You don't have enough money.")
        """),
        ("Get a boy dog", """
if You.money >= 175:
  You.money -= 175
  dog = Dog(random.choice(boy_pet_names, random.randint(0, 4), "Male", You)
  You.pets.append(dog)
else:
  print("You don't have enough money.")
        """),
        ("Get a girl dog", """
if You.money >= 175:
  You.money -= 175
  dog = Dog(random.choice(girl_pet_names, random.randint(0, 4), "Female", You)
  You.pets.append(dog)
else:
  print("You don't have enough money.")
        """)
      ]
    }
    shelter = EventNode("Animal Shelter", dic)
    G.add_node(shelter)
    G.add_edge(pet, shelter)
    dic = {
      "You went to the pet store. It costs $175 for a cat or a dog." : [
        ("Get a boy cat", """
    if You.money >= 175:
    You.money -= 175
    cat = Cat(random.choice(boy_pet_names, random.randint(0, 4), "Male", You)
    You.pets.append(cat)
    else:
    print("You don't have enough money.")
        """),
        ("Get a girl cat", """
    if You.money >= 175:
    You.money -= 175
    cat = Cat(random.choice(girl_pet_names, random.randint(0, 4), "Female", You)
    You.pets.append(cat)
    else:
    print("You don't have enough money.")
        """),
        ("Get a boy dog", """
    if You.money >= 175:
    You.money -= 175
    dog = Dog(random.choice(boy_pet_names, random.randint(0, 4), "Male", You)
    You.pets.append(dog)
    else:
    print("You don't have enough money.")
        """),
        ("Get a girl dog", """
    if You.money >= 175:
    You.money -= 175
    dog = Dog(random.choice(girl_pet_names, random.randint(0, 4), "Female", You)
    You.pets.append(dog)
    else:
    print("You don't have enough money.")
        """)
      ]
    }
    petstore = EventNode("Pet Store", dic)
    G.add_node(petstore)
    G.add_edge(pet, petstore)
  if node.key == 18:
    vacation = EventCategory("Vacation")
    G.add_node(vacation)
    G.add_edge(Activiies, vacation)
    dic = {
      "Which vacation do you want to go on? Each vacation costs different ammounts." : [
        ("Go to Nassau, Bahamas. It costs $3000.", """
if You.money >= 3000:
  You.money -= 3000
  You.happiness += 30
  print("I went to Nassau, Bahamas. I gained 30 happiness.")
else:
  print("You don't have enough money.")
        """),
        ("Go to Honolulu, Hawaii. It costs $4000.", """
if You.money >= 4000:
  You.money -= 4000
  You.happiness += 40
  print("I went to Honolulu, Hawaii. I gained 40 happiness.")
else:
  print("You don't have enough money.")
        """),
        ("Go to Miami, Flordia. It costs $2000.", """
if You.money >= 2000:
  You.money -= 2000
  You.happiness += 20
  print("I went to Miami, Flordia. I gained 20 happiness.")
else:
  print("You don't have enough money.")
        """),
        ("Go to ???. It costs $10000.", """
if You.money >= 10000:
  You.money -= 10000
  You.happiness += 50
  print("I went to ???. I gained 50 happiness.")
        """),
        ("Go to Tel Aviv, Isreal. It costs $1000.", """
if You.money >= 1000:
  You.money -= 1000
  You.happiness += 70
  print("I went to Tel Aviv, Isreal. I gained 70 happiness.")
else:
  print("You don't have enough money.")
        """),
        ("Go to Toronto, Canada. It costs $5000.", """
if You.money >= 5000:
  You.money -= 5000
  You.happiness += 25
  print("I went to Toronto, Canada. I gained 25 happiness.")
else:
  print("You don't have enough money.")
        """)
      ]
    }
    airplane = EventNode("Airplane", dic)
    G.add_node(airplane)
    G.add_edge(vacation, airplane)
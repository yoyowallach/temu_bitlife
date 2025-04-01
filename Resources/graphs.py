# graphs.py

import tkinter as tk
from Resources.classes import Graph, EventNode, AgeNode, MainMenu, EventCategory, Cat, Dog
import random
from main import Mother, Father, Sister, You, Brother
from Resources.data_structures import sponsors, sickness, boy_pet_names, girl_pet_names

G = Graph()

# -------------------------------------------------------

Activiies = MainMenu("Activiies")
for i in range(0, 30):
  AgeRoot = AgeNode(i)
  G.agenodes.(AgeRoot)
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
cat = Cat(random.choice(boy_pet_names)
        """),
        ("Get a girl cat 2", "print('Option 2')"),
        ("Get a boy dog", "print('Option 1')"),
        ("Get a girl dog", "print('Option 1')")
      ]
    }
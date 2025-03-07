# graphs.py

import tkinter as tk
from Resources.classes import EventNode, AgeNode, MainMenu, EventCategory, Graph

G = Graph()

# -------------------------------------------------------

Occupation = MainMenu("Occupation")
G.add_node(Occupation)
Assets = MainMenu("Assets")
G.add_node(Assets)
Relationships = MainMenu("Relationships")
G.add_node(Relationships)
Activiies = MainMenu("Activiies")
G.add_node(Activiies)

# -------------------------------------------------------

for i in range(0, 30):
  AgeRoot = AgeNode(i)
  G.add_node(AgeRoot)
  G.add_edge(AgeRoot, Occupation)
  G.add_edge(AgeRoot, Assets)
  G.add_edge(AgeRoot, Relationships)
  G.add_edge(AgeRoot, Activiies)

# -------------------------------------------------------

class EventNode:
  def __init__(self, key, dic):
    self.key = key
    self.dic = dic
    self.neighbors = []
  def add_neighbor(self, node):
    self.neighbors.append(node)
  def display_choices(self):
    print("\n\n")
    print(self.dic[])

dic = {
  "Main Message" : [
    ("Question Text", "Code"),
    ("Question Text", "Code")
  ]
}
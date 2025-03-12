# graphs.py

import tkinter as tk
from classes import Graph, EventNode, AgeNode, MainMenu, EventCategory

G = Graph()

# -------------------------------------------------------

Activiies = MainMenu("Activiies")
for i in range(0, 30):
  AgeRoot = AgeNode(i)
  G.agenodes.add(AgeRoot)
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


for node in G.agenodes:
  if node.key == 0:
    doctor = EventCategory("Doctor")
    G.add_node(doctor)
    G.add_edge(Activiies, doctor)
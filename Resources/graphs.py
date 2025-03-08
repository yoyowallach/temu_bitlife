# graphs.py

import tkinter as tk

G = Graph()

# -------------------------------------------------------

for i in range(0, 30):
  AgeRoot = AgeNode(i)
  Occupation = MainMenu("Occupation")
  G.add_node(Occupation)
  Assets = MainMenu("Assets")
  G.add_node(Assets)
  Relationships = MainMenu("Relationships")
  G.add_node(Relationships)
  Activiies = MainMenu("Activiies")
  G.add_node(Activiies)
  G.add_node(AgeRoot)
  G.add_edge(AgeRoot, Occupation)
  G.add_edge(AgeRoot, Assets)
  G.add_edge(AgeRoot, Relationships)
  G.add_edge(AgeRoot, Activiies)
  
# -------------------------------------------------------


# classes.py

from main import Mother, Father, Sister, You, Brother
from data_structures import BN, GN, basicjobs 

class Job:
  def __init__(self, name, salary, company, position, positions):
      self.name = name
      self.salary = salary
      self.company = company
      self.position = position
      self.positions = positions

# -------------------------------------------------------

class Brotherwhoisnotalive:
  def __init__(self):
      self.age = 1
      self.posnumber = 1000

# -------------------------------------------------------

class Person:
  def __init__(self, fn, ln, age, relation, gender, city, country, job, posnumber, money, relationstatus):
      self.fn = fn
      self.ln = ln
      self.age = age
      self.relation = relation
      self.gender = gender
      self.city = city
      self.country = country
      self.job = job
      self.job_title, self.salary = self.job.positions[posnumber-1]
      self.carlisence = False
      self.possessions = []
      self.money = money
      self.health = 100
      self.happiness = 100
      self.smarts = 100
      self.looks = 100
      if self.relation == "You":
        self.relationstatus = 100
      self.relationstatus = relationstatus
      self.sickness = []
  def ageyear(self):
      self.age += 1
      Mother.age += 1
      Father.age += 1
      Sister.name += 1
      if Brother.posnumber != "10000":
          Brother.age += 1
          Brother.money += Brother.salary
      Mother.money += Mother.salary
      Father.money += Father.salary
      Sister.money += Sister.salary
      self.money += self.salary
  def promotion(self):
      if self.job.name != "Jobless":
          self.posnumber += 1 
          newjobinfo = self.job.positions[posnumber-1]
          self.job_title, self.salary = newjobinfo
          print("promo completed")

# -------------------------------------------------------

class Car:
  def __init__(self, price, owner, condition, age, model):
      self.price = price
      self.owner = owner
      self.condition = condition
      self.age = age
      self.model = model
      self.type = "Car"
  def buy(self, buyer):
      if buyer.money >= self.price:
          buyer.money -= self.price
          if buyer.carlisence == True:
              print(f"I bought a {self.model} for {self.price} dollars.")
              buyer.possessions.append(self)
          else:
              print("I tried to buy a car, but I dont have a licence.")

# -------------------------------------------------------

class peoplenil:
  def __init__(self, fn, ln, age, money, job, posnumber, relation):
      self.fn = fn
      self.ln = ln
      self.age = age
      self.money = money
      self.job = job
      self.job_title, self.salary = self.job.positions[posnumber-1]
      self.health = health
      self.smarts = random.randint(1, 100)
      self.health = random.randint(1, 100)
      self.craziness = random.randint(1, 100)
      self.relation  = relation
  def promotion(self):
      if self.job.name != "Jobless":
          self.posnumber += 1
          newjobinfo = self.job.positions[posnumber]
          self.job_title, self.salary = newjobinfo
          print("promo completed")

# -------------------------------------------------------

class Cat:

# -------------------------------------------------------

class EventNode:
  def __init__(self, key, dic):
    self.key = key
    self.dic = dic
    self.neighbors = []
  def add_neighbor(self, node):
    self.neighbors.append(node)
  def display_choices(self):
    counter = 1
    print("\n")
    for item in self.dic:
      print(item)
      print("\nOptions:")
      for items in self.dic[item]:
        print(f"Option number {counter}: {items[0]}")
        counter += 1
    choice = int(input("\n\nWhat do you want to do? (Enter the number of the option)\n "))
    while choice > len(self.dic[item]):
      choice = int(input("\n\nWhat do you want to do? (Enter the number of the option)\n "))
    print("\n")
    exec(self.dic[item][choice-1][1])
  def __str__(self):
    self.display_choices()
    return ""

# dic = {
#   "Main Message" : [
#     ("Question Text", "print('Hello world!')"),
#     ("Question Text", "print('Option 2')"),
#     ("Question Text", "print('Option 3')")
#   ]
# }

# -------------------------------------------------------

class AgeNode:
  def __init__(self, key):
    self.key = key
    self.neighbors = []
  def add_neighbor(self, node):
    self.neighbors.append(node)

# -------------------------------------------------------

class MainMenu:
  def __init__(self, key):
    self.key = key
    self.neighbors = []
  def add_neighbor(self, node):
    self.neighbors.append(node)

# -------------------------------------------------------

class EventCategory:
  def __init__(self, key):
    self.key = key
    self.neighbors = []
  def add_neighbor(self, node):
    self.neighbors.append(node)

# -------------------------------------------------------

class Graph:
  def __init__(self):
    self.graph = {}
    self.agenodes = {}
  def add_node(self, node):
    self.graph[node.key] = node
  def add_edge(self, node1, node2):
    if node1.key in self.graph and node2.key in self.graph:
      node1.add_neighbor(node2)
    else:
      print("One of the nodes does not exist in the graph.\n Error 001.")
  def find_node_by_key(self, age):
    for node in self.graph:
      if node.key == age:
        return node
# -------------------------------------------------------

doctor = Job("Doctor", 110000, "Bob Hospitals, Inc", "Junior Doctor", [("Junior Doctor", 110000) ,("Doctor", 120000), ("Senior Doctor", 140000), ("Head Doctor", 170000)])
lawyer = Job("Lawyer", 90000, "Bob, Joe & Fred", "Junior Attorney", [("Junior Attorney", 90000), ("Attorney", 110000), ("Senior Attorney", 130000), ("Head Attorney", 160000)])
engineer = Job("Engineer", 80000, "Bob Construction, Inc", "Junior Engineer", [("Junior Engineer", 80000), ("Engineer", 90000), ("Head Engineer", 120000), ("Head Engineer", 150000)])
teacher = Job("Teacher", 63000, "Bob Elementaty School", "Kindergarten Teacher", [("Kindergarten Teacher", 63000), ("First Grade Teacher", 68000), ("Second Grade Teacher", 73000), ("Third Grade Teacher", 78000), ("Fourth Grade Teacher", 83000), ("Fifth Grade Teacher", 88000), ("Vice Princical", 98000), ("Principal", 5)])
jobless = Job("Jobless", 10000, "Nobody", "NA", [("Jobless", 10000)])
storeworker = Job("Storeworker", 28000, "Bob Grocery", "Junior Cashier", [("Junior Cashier", 28000), ("Cahier", 38000), ("Senior Cashier", 45000), ("Head Cashier", 50000)])
joblessK = Job("Jobless", 0, "NA", "NA", [("NA", 0)])
basicjobs = [doctor, lawyer, engineer, teacher, storeworker]

# -------------------------------------------------------
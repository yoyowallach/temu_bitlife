class Person:
  def __init__(self, fn, ln, age, relation, gender, city, country, job, posnumber, money):
      self.fn = fn
      self.ln = ln
      self.age = age
      self.relation = relation
      self.gender = gender
      self.city = city
      self.country = country
      self.job = job
      self.job_title, self.salary = self.job.positions[0]
  def age(self):
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
          self.posnumber += 1-1
          newjobinfo = self.job.positions[self.posnumber]
          self.job_title, self.salary = newjobinfo
          print("promo completed")
# class Event:
#     def __init__(self, agelock, ageIA, text, o1t, o2t, UP, person, FR, o1m, o2m):
#         self.agelock = agelock
#         self.ageIA = ageIA
#         self.text = text
#         self.o1t = o1t
#         self.o2t = o2t
#         self.UP = UP
#         # uses person
#         self.person = person
#         self.fr = FR
#         # friend request
#         self.o1m = o1m
#         self.o2m = o2m

def askforfriend(person):
  print(f"{person.fn} {person.ln} would like to become your friend!")
  while True:
      choice = input("Option 1: Accept them.\nOption 2: Reject them.\nEnter 1 or 2 below.\n")
      if choice == "1":
          # only cuz dey got dat money
          print(f"{person.fn} is now your friend!")
          person.relation == "Friend"
          return person
      elif choice == "2":
          # hail no cuz dey not da handsome
          print(f"You rejected {person.fn} as your friend.")
          break
      else:
          # why u not following da rules? i dont understand???
          print("Please enter 1 or 2.")

Yotam = Person("Yotam", "Wallach", 1, "Hero", "M", "Albany", "United States", doctor, 1)
print("Hello")
print(askforfriend(Yotam))
print("Hi")
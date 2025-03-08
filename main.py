# main.py


# import packages

from Resources.functions import generate_family
Mother, Father, Sister, You, Brother = generate_family("Yotam", "Wallach", "Albany", "M")
from Resources.classes import EventNode

dic = {
  "You move to a new city" : [
    ("Protest to your parents", "print('Option 1')"),
    ("Go without complaint", "print('Option 2')"),
    ("Be exited", "print('Option 3')")
  ]
}
zero0 = EventNode("00", dic)
print(zero0)
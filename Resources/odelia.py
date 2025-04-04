# odelia.py


from classes import EventNode

'''
1. Copy the template

dic = {
  "Message" : [
    ("Option 1", "print('Option 1')"),
    ("Option 2", "print('Option 2')")
  ]
}

add or remove options, dont forget the comma!

make the class, the first digit should be in full form, 2nd digit in simplified form.

ie. zero1

digit 1 is age
digit 2 is number in age

then make the node

ie. 
zero1 = EventNode("key", dic)
make the node under the dictonary

key should be the name, 1 digit in full form, 1 in number form
replace dic with your entire dictonary
make sure to write comments telling me what to do
'''

# -------------------------------------------------------

zero1 = EventNode("zero1", {
                   "You are saying your first words" : [
                     ("Say mama", "print('Option 1')"), # +5 for your realationship with your mom
                     ("Say dada", "print('Option 2')"), # +5 for your realationship with your dad
                   ]
                 })

zero2 = EventNode("zero2", {
                   "You are taking your first steps" : [
                     ("Hold the chair for balance", "print('Option 1')"), #   print "You sucssesfully stood up"
                     ("Try to stand up without holding on to anything", "print('Option 2')"), # 50 50 chance you fall and loose -3 health or you stand up and print "You sucssesfully stood up"
                   ]
                 })
# -------------------------------------------------------

one1 = EventNode("one1", {
                  "First Time at the Zoo" : [
                    ("Point excitedly at the animals", "print('Option 1')"), # +5 happiness
                    ("Cry because the animals are scary", "print('Option 2')") # -5 happiness
                  ]
                })


one2 = EventNode("one2", {
                  "Learning to Feed Yourself" : [
                    ("Use the spoon", "print('Option 1')"), # +10 smarts
                    ("Throw food on the floor", "print('Option 2')") # -10 relaition with mom
                  ]
                })
# -------------------------------------------------------


two1 = EventNode("two1", {
                   "Your Parents Want to Potty Train You" : [
                     ("Embrace the training eagerly", "print('Option 1')"), # +5 smarts
                     ("Resist stubbornly", "print('Option 2')") # -5 relaition with mom and dad
                   ]
                 }

two2 = EventNode("two2", {
                 "Your parents say no to going to Micdonalds" : [
                   ("Scream until you get what you want", "print('Option 1')"), # -5 relaition with mom and dad
                   ("calm down quickly", "print('Option 2')") # +5 relaition with mom and dad
                 ]
                })

# -------------------------------------------------------

dic = {
  "Your Ice Cream Fell On The Floor" : [
    ("Cry", "print('Option 1')"), # -5 relaition with mom and dad
    ("Ask for a new cone", "print('Option 2')") # +5 hapiness
  ]
}
three1 = EventNode("three1", {
                    "Your Ice Cream Fell On The Floor" : [
                      ("Cry", "print('Option 1')"), # -5 relaition with mom and dad
                      ("Ask for a new cone", "print('Option 2')") # +5 hapiness
                    ]
                  })

dic = {
  "First Day of Preschool" : [
    ("Cry when parents leave", "print('Option 1')"), # -5 hapiness
    ("Make friends immediately", "print('Option 2')") # +5 hapiness
  ]
}


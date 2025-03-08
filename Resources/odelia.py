# odelia.py


from Resources.classes import EventNode

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
zero1 = EventNode(key, dic)
make the node under the dictonary

key should be the name, 1 digit in full form, 1 in number form
replace dic with your entire dictonary
make sure to write comments telling me what to do
'''

# -------------------------------------------------------

zero1 = EventNode(zero1, dic = {
                   "You are saying your first words" : [
                     ("Say mama", "print('Option 1')"), # +5 for your realationship with your mom
                     ("Say dada", "print('Option 2')"), # +5 for your realationship with your dad
                   ]
                 })

zero2 = EventNode(zero2, dic = {
                   "You are taking your first steps" : [
                     ("Hold the chair for balance", "print('Option 1')"), #   print "You sucssesfully stood up"
                     ("Try to stand up without holding on to anything", "print('Option 2')"), # 50 50 chance you fall and loose -3 health or you stand up and print "You sucssesfully stood up"
                   ]
                 })
# -------------------------------------------------------
print(zero1)
print(zero2)


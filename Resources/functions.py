# functions.py

import tkinter as tk
import random
from data_structures import BN, GN, LN, sponsors
from classes import Person, Brotherwhoisnotalive, basicjobs, joblessK

# -------------------------------------------------------

def display_message_with_buttons(entry):
    if isinstance(entry, tuple) and len(entry) == 2:
        message, choices = entry
        root = tk.Tk()
        root.title("Message with Buttons")

        message_box = tk.Text(root, height=5, width=40)
        message_box.pack(pady=10)
        message_box.insert(tk.END, message)
        message_box.config(state=tk.DISABLED)

        def on_button_click(choice):
            print(f"Button {choice[0]} clicked!")
            exec(choice[1])
            root.quit()

        for choice in choices:
            if isinstance(choice, tuple) and len(choice) == 2:
                button = tk.Button(root, text=choice[0], command=lambda choice=choice: on_button_click(choice))
                button.pack(pady=5)

        root.mainloop()
    else:
        print("Invalid input format. Ensure it is a tuple with [message, choices].")

# dic = {
#   "Main Message" : [
#     ("Question Text", "print('Hello world!')"),
#     ("Question Text", "print('Option 2')"),
#     ("Question Text", "print('Option 3')")
#   ]
# }

# -------------------------------------------------------

# def display_ads(adcounter):
#     ads_played = []
#     sponsor_keys = list(sponsors.keys())
#     ads_to_display = adcounter
#     ads_displayed = 0
#     while ads_displayed < ads_to_display:
#         if len(ads_played) >= len(sponsor_keys):
#             ads_played = []        
#         available_sponsors = [key for key in sponsor_keys if key not in ads_played]
#         if available_sponsors:
#             sponsor_key = random.choice(available_sponsors)
#             print(f"AD {ads_displayed + 1}/{ads_to_display}:")
#             print(sponsors[sponsor_key])
#             print("\n\n")
#             ads_played.append(sponsor_key)
#             ads_displayed += 1

# -------------------------------------------------------

def friend_request(person, adcounter):
    print(f"{person.fn} {person.ln} would like to become your friend!")
    while True:
        choice = input("To accept, input 1.\nTo reject them, input 2.\n")
        if choice == "1":
            break
        elif choice == "2":
            break
        else:
            print("Please say 1 or 2. An extra ad will be displayed sometime")
            adcounter += 1
    if int(choice) == 1:
        person.relation = ""
        person.relation = "Friend"
        print(f"{person.fn} is now your friend!")
        return adcounter
    elif int(choice) == 2:
        print(f"You rejected {person.fn}.")
        return adcounter

# -------------------------------------------------------

def generate_family(name, lastname, city, gender):
    momname = random.choice(GN)
    GN.remove(momname)
    Mother = Person(momname, lastname, random.randint(21, 51), "Mother", "F", city, "United States", random.choice(basicjobs), random.choice(jobposnumbers), random.randint(1257, 10000000), 100)
    dadname = random.choice(BN)
    Father = Person(dadname, lastname, random.randint(21, 51), "Father", "M", city, "United States",random.choice(basicjobs), random.choice(jobposnumbers), random.randint(1257, 10000000), 100)
    sisname = random.choice(GN)
    GN.remove(sisname)
    Sister = Person(sisname, lastname, 3, "Sister", "F", city, "United States", joblessK, 1, 500, 100)
    You = Person(name, lastname, 0, "You", gender, city, "United States", joblessK, 1, 0, 100)
    Brother = Brotherwhoisnotalive()
    return(Mother, Father, Sister, You, Brother)

# -------------------------------------------------------

global jobposnumbers
jobposnumbers = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

# -------------------------------------------------------

def display_message(message):
    root = tk.Tk()
    root.title("Message")
    message_box = tk.Text(root, height=5, width=40)
    message_box.pack(pady=10)
    message_box.insert(tk.END, message)
    message_box.config(state=tk.DISABLED)
    def close_window():
        root.quit()
    ok_button = tk.Button(root, text="OK", command=close_window)
    ok_button.pack(pady=5)
    root.mainloop()
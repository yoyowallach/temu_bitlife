# graphs.py

import tkinter as tk


class EventNode:
  def __init__(self, key, dic):
    self.key = key
    self.dic = dic
  def display_message_with_buttons(self, entry):
    if isinstance(entry, tuple) and len(entry) == 2:
      message, choices = entry
      root = tk.Tk()
      root.title("Message with Buttons")

      message_box = tk.Text(root, height=5, width=40)
      message_box.pack(pady=10)
      message_box.insert(tk.END, message)
      message_box.config(state=tk.DISABLED)

      def on_button_click(choice):
        exec(choice[1])
        root.destroy()

      for choice in choices:
        if isinstance(choice, tuple) and len(choice) == 2:
          button = tk.Button(root, text=choice[0], command=lambda choice=choice: on_button_click(choice))
          button.pack(pady=5)
          
      root.mainloop()
    else:
        print("Invalid input format. Ensure it is a tuple with [message, choices].")
  def __str__(self):
    self.display_message_with_buttons(self.dic[1])
    return ""
o1 = {
  1: ("You find a toy", [
    ("Take it", "print('took it')"),
    ("throw it away", "print('throwed it')")
  ])
}

option1 = EventNode("Toy", o1)

print(option1)
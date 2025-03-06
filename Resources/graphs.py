# graphs.py


import tkinter as tk

class EventNode:
  def __init__(self, key, message, options, optioncode):
      self.key = key
      self.message = message
      self.options = options
      self.optioncode = optioncode

  def __str__(self):
    root = tk.Tk()
    root.title("Event")

    message_box = tk.Text(root, height=5, width=40)
    message_box.pack(pady=10)
    message_box.insert(tk.END, self.message)
    message_box.config(state=tk.DISABLED)

    output_box = tk.Text(root, height=5, width=40)
    output_box.pack(pady=10)
    output_box.config(state=tk.DISABLED)

    def on_button_click(index):
        try:
            local_scope = {}
            exec(self.optioncode[index], {}, local_scope)
            output_box.config(state=tk.NORMAL)
            output_box.delete(1.0, tk.END)
            output_box.insert(tk.END, str(local_scope.get("output", "Executed")))
            output_box.config(state=tk.DISABLED)
            root.destroy()  # Close the window after execution
        except Exception as e:
            output_box.config(state=tk.NORMAL)
            output_box.insert(tk.END, f"Error: {e}\n")
            output_box.config(state=tk.DISABLED)

    for i, option in enumerate(self.options):
        button = tk.Button(root, text=option, command=lambda i=i: on_button_click(i))
        button.pack(pady=5)

    root.mainloop()
    return ""  # To satisfy __str__ return requirement

option1 = EventNode("ToyEvent" ,"You find a toy", ["You keep the toy", "You throw the toy away"], ["""
print("Hi")
for i in range(10):
  print(i+12)
""", """
vars = 10
print(vars)
"""])
print(option1)
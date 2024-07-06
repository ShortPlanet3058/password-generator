import tkinter as tk
from tkinter import Entry, Label, Button, StringVar
import random
import string

def generate_password():
    password_length = int(length_var.get())

    if password_length < 4:
        password_var.set("Password length must be at least 4")
        return

    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    generated_password = ''.join(random.choice(chars) for _ in range(password_length))
    password_var.set(generated_password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure the widgets
Label(root, text="Password Length:").pack()
length_var = StringVar()
length_entry = Entry(root, textvariable=length_var)
length_entry.pack()

Label(root, text="Include Digits:").pack()
digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, variable=digits_var)
digits_check.pack()

Label(root, text="Include Special Characters:").pack()
special_chars_var = tk.BooleanVar()
special_chars_check = tk.Checkbutton(root, variable=special_chars_var)
special_chars_check.pack()

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_var = StringVar()
password_label = Label(root, textvariable=password_var)
password_label.pack()

# Add label at the bottom right
author_label = Label(root, text="By ShortPlanet3058", anchor="e", foreground="gray")
author_label.pack(side="bottom", fill="x")

# Run the application
root.mainloop()
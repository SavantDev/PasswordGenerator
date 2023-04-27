import random
import string
import tkinter as tk

# Define the password generator function
def generate_password(length=12, include_digits=True, include_symbols=True):
    # Define the character sets to use
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits if include_digits else ""
    symbols = string.punctuation if include_symbols else ""

    # Combine the character sets based on the user's preferences
    valid_chars = uppercase_letters + lowercase_letters + digits + symbols

    # Generate the password
    password = "".join(random.choice(valid_chars) for _ in range(length))

    return password

# Define the GUI class
class PasswordGeneratorGUI:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Password Generator")

        # Create the widgets
        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_entry = tk.Entry(self.root, width=10)
        self.length_entry.insert(0, "12")
        self.digits_checkbutton = tk.Checkbutton(self.root, text="Include Digits")
        self.symbols_checkbutton = tk.Checkbutton(self.root, text="Include Symbols")
        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.password_label = tk.Label(self.root, text="Your password will appear here.")

        # Lay out the widgets
        self.length_label.grid(row=0, column=0)
        self.length_entry.grid(row=0, column=1)
        self.digits_checkbutton.grid(row=1, column=0)
        self.symbols_checkbutton.grid(row=1, column=1)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.password_label.grid(row=3, column=0, columnspan=2)

    def generate_password(self):
        # Get the user's preferences from the GUI
        length = int(self.length_entry.get())
        include_digits = self.digits_checkbutton.instate(["selected"])
        include_symbols = self.symbols_checkbutton.instate(["selected"])

        # Generate and display the password
        password = generate_password(length, include_digits, include_symbols)
        self.password_label.config(text=f"Your password is: {password}")

    def run(self):
        # Start the main event loop
        self.root.mainloop()

# Create an instance of the PasswordGeneratorGUI class and run it
gui = PasswordGeneratorGUI()
gui.run()

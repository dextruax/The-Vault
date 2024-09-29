import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import datetime

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.geometry("800x600")
        self.current_account = None
        self.passwords = {}  # Store passwords in a dictionary

        self.setup_gui()

    def setup_gui(self):
        # Create a style using ttkbootstrap
        style = ttk.Style()
        style.configure("TButton", borderwidth=2, relief="flat", padding=(5, 5))
        
        # Create folder tree on the left
        self.folder_tree = ttk.Treeview(self.master, height=15)
        self.folder_tree.grid(row=0, column=0, sticky='nsew')

        # Create a frame for the password table
        self.password_frame = ttk.Frame(self.master)
        self.password_frame.grid(row=0, column=1, sticky='nsew')

        # Create a table for displaying passwords
        self.password_table = ttk.Treeview(self.password_frame)
        self.password_table.pack(expand=True, fill='both')

        # Create password generator controls
        self.setup_password_generator()

        # Create folder structure, load passwords
        self.load_folder_structure()
        self.load_passwords()

    def setup_password_generator(self):
        # Slider for password length
        self.length_slider = tk.Scale(self.master, from_=1, to=256, orient='horizontal', label='Password Length')
        self.length_slider.set(32)  # Default length
        self.length_slider.grid(row=1, column=0, sticky='ew')

        # Character options
        self.character_options_frame = ttk.Frame(self.master)
        self.character_options_frame.grid(row=2, column=0)

        self.letters_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=False)

        ttk.Checkbutton(self.character_options_frame, text="Include Letters", variable=self.letters_var).pack(side='left')
        ttk.Checkbutton(self.character_options_frame, text="Include Numbers", variable=self.numbers_var).pack(side='left')
        ttk.Checkbutton(self.character_options_frame, text="Include Special Characters", variable=self.special_var).pack(side='left')

        # Generate password button
        self.generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0)

        # Copy button for the generated password
        self.copy_button = ttk.Button(self.master, text="Copy Password", command=self.copy_password)
        self.copy_button.grid(row=3, column=1)

    def load_folder_structure(self):
        # Create a sample folder structure (this will need to be dynamic)
        self.folder_tree.insert("", "end", "google", text="Google")
        self.folder_tree.insert("google", "end", "work_google", text="Work Google Account")
        self.folder_tree.insert("google", "end", "school_google", text="School Google Account")

        # Bind selection event
        self.folder_tree.bind("<<TreeviewSelect>>", self.on_folder_select)

    def on_folder_select(self, event):
        # Load passwords for the selected account
        selected_item = self.folder_tree.selection()[0]
        self.current_account = self.folder_tree.item(selected_item)['text']
        self.load_passwords()

    def load_passwords(self):
        # Clear the password table
        for row in self.password_table.get_children():
            self.password_table.delete(row)

        # Dummy data for testing
        if self.current_account == "Work Google Account":
            passwords = [("username1", "password1", "2023-01-01"),
                         ("username2", "password2", "2023-02-01")]
        elif self.current_account == "School Google Account":
            passwords = [("username3", "password3", "2023-03-01")]

        # Insert passwords into the table
        for username, password, date in passwords:
            self.password_table.insert("", "end", values=(username, password, date))

    def generate_password(self):
        length = self.length_slider.get()
        include_letters = self.letters_var.get()
        include_numbers = self.numbers_var.get()
        include_special = self.special_var.get()

        # Generate password logic here (use random and string modules)
        password = "GeneratedPassword"  # Placeholder

        # Show the generated password
        self.generated_password = password

    def copy_password(self):
        # Copy the generated password to clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()
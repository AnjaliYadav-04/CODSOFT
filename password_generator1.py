import tkinter as tk
import random
import string
import base64
import json
from tkinter import ttk, messagebox

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator and Manager")
        self.master.geometry("400x500")

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=20)

        self.generator_frame = ttk.Frame(self.notebook)
        self.manager_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.generator_frame, text="Generator")
        self.notebook.add(self.manager_frame, text="Manager")

        self.setup_generator()
        self.setup_manager()
        self.load_password()

    def setup_generator(self):
        self.length_var = tk.StringVar(value="12")
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar()

        ttk.Label(self.generator_frame, text="Password Length:").pack(pady=5)
        ttk.Entry(self.generator_frame, textvariable=self.length_var, width=5).pack()

        ttk.Checkbutton(self.generator_frame, text="Uppercase", variable=self.uppercase_var).pack()
        ttk.Checkbutton(self.generator_frame, text="Lowercase", variable=self.lowercase_var).pack()
        ttk.Checkbutton(self.generator_frame, text="Numbers", variable=self.numbers_var).pack()
        ttk.Checkbutton(self.generator_frame, text="Symbols", variable=self.symbol_var).pack()

        ttk.Button(self.generator_frame, text="Generate Password", command=self.generate_password).pack(pady=10)
        ttk.Entry(self.generator_frame, textvariable=self.password_var, state="readonly").pack()
        ttk.Button(self.generator_frame, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=10)

    def setup_manager(self):
        self.service_var = tk.StringVar()
        self.username_var = tk.StringVar()
        self.password_name_var = tk.StringVar()

        ttk.Label(self.manager_frame, text="Service").pack(pady=5)
        ttk.Entry(self.manager_frame, textvariable=self.service_var, width=30).pack()

        ttk.Label(self.manager_frame, text="Username").pack(pady=5)
        ttk.Entry(self.manager_frame, textvariable=self.username_var, width=30).pack()

        ttk.Label(self.manager_frame, text="Password").pack(pady=5)
        ttk.Entry(self.manager_frame, textvariable=self.password_name_var, width=30).pack()

        ttk.Button(self.manager_frame, text="Save Password", command=self.save_password).pack(pady=5)

        self.password_tree = ttk.Treeview(self.manager_frame, columns=("Service", "Username"), show='headings')
        self.password_tree.heading("Service", text="Service")
        self.password_tree.heading("Username", text="Username")
        self.password_tree.pack(pady=5)
        self.password_tree.bind("<Double-1>", self.on_tree_double_click)

    def generate_password(self):
        length = int(self.length_var.get())
        characters = ""

        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.numbers_var.get():
            characters += string.digits
        if self.symbol_var.get():
            characters += string.punctuation

        if not characters:
            self.password_var.set("Please select at least one character type")
        else:
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)

    def copy_to_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.password_var.get())
        self.master.update()

    def save_password(self):
        service = self.service_var.get()
        username = self.username_var.get()
        password = self.password_name_var.get()

        if service and username and password:
            encrypted_password = self.encrypt(password)
            self.password[service] = {"username": username, "password": encrypted_password}
            self.save_password_to_file()
            self.update_password_tree()
            messagebox.showinfo("Success", "Password saved successfully")
            self.service_var.set("")
            self.username_var.set("")
            self.password_name_var.set("")
        else:
            messagebox.showerror("Error", "All fields are required")

    def save_password_to_file(self):
        with open("passwords.json", "w") as f:
            json.dump(self.password, f)

    def load_password(self):
        try:
            with open("passwords.json", "r") as f:
                self.password = json.load(f)
        except FileNotFoundError:
            self.password = {}
        self.update_password_tree()

    def update_password_tree(self):
        for item in self.password_tree.get_children():
            self.password_tree.delete(item)
        for service, data in self.password.items():
            self.password_tree.insert("", "end", values=(service, data["username"]))

    def on_tree_double_click(self, event):
        item = self.password_tree.selection()[0]
        service = self.password_tree.item(item, "values")[0]
        username = self.password[service]["username"]
        encrypted_password = self.password[service]["password"]
        password = self.decrypt(encrypted_password)
        messagebox.showinfo("Password", f"Service: {service}\nUsername: {username}\nPassword: {password}")

    def encrypt(self, password):
        return base64.b64encode(password.encode()).decode()

    def decrypt(self, encrypted_password):
        return base64.b64decode(encrypted_password.encode()).decode()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

from tkinter import *
from tkinter import messagebox, simpledialog, ttk
import json
import os

class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Login")
        self.geometry("400x300")

        s = ttk.Style()
        s.configure('TFrame', background="blue")

        header_frame = ttk.Frame(self, style='TFrame')
        header_frame.pack(fill=X)

        s.configure('TLabel', background='blue', foreground='white', font=('Arial', 25))

        header_label = ttk.Label(header_frame, text="My Contact Book")
        header_label.pack()

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show='*')
        self.password_entry.pack(pady=5)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        self.contacts = {}
        self.load_contacts()

    def login(self):
        # Simple login check (username: user, password: pass)
        if self.username_entry.get() == "user" and self.password_entry.get() == "pass":
            self.destroy()  # Close login window
            self.open_contact_book()
        else:
            messagebox.showerror("Login failed", "Invalid username or password.")

    def open_contact_book(self):
        self.contact_book = ContactBook(self.contacts)
        self.contact_book.mainloop()

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
        else:
            self.contacts = {}

class ContactBook(Tk):
    def __init__(self, contacts):
        super().__init__()

        self.title("Contact Book")
        self.geometry("500x400")

        self.contacts = contacts

        self.contact_listbox = Listbox(self, width=50, height=15)
        self.contact_listbox.pack(pady=20)

        self.add_contact_button = Button(self, text="Add Contact", command=self.add_contact)
        self.add_contact_button.pack(pady=5)

        self.delete_contact_button = Button(self, text="Delete Contact", command=self.delete_contact)
        self.delete_contact_button.pack(pady=5)

        self.update_contact_list()

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter contact phone number:")
            if phone:
                self.contacts[name] = phone
                self.save_contacts()
                self.update_contact_list()

    def delete_contact(self):
        selected_contact = self.contact_listbox.curselection()
        if selected_contact:
            contact_name = self.contact_listbox.get(selected_contact)
            del self.contacts[contact_name]
            self.save_contacts()
            self.update_contact_list()
        else:
            messagebox.showwarning("Selection Error", "No contact selected.")

    def update_contact_list(self):
        self.contact_listbox.delete(0, END)
        for name in self.contacts:
            self.contact_listbox.insert(END, name)

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump(self.contacts, f)

if __name__ == "__main__":
    lw = LoginWindow()
    lw.mainloop()


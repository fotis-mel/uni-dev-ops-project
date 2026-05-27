import tkinter as tk
from tkinter import messagebox


class MechanicGUI:
    def __init__(self, management, username, parent):
        self.mgmt = management
        self.username = username
        self.root = tk.Toplevel(parent)
        self.root.title("Mechanic Screen")
        self.root.geometry("400x300")

        tk.Label(
            self.root,
            text=f"Συνδεδεμένος: {username}",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(self.root, text="Αίτηση Άδειας", command=self.request_leave).pack(pady=10)
        tk.Button(self.root, text="Αίτηση Ανταλλακτικών", command=self.request_parts).pack(pady=10)
        tk.Button(self.root, text="Αποσύνδεση", command=self.root.destroy).pack(pady=10)

    def request_leave(self):
        messagebox.showinfo("Άδεια", "Στάλθηκε ✔")

    def request_parts(self):
        messagebox.showinfo("Ανταλλακτικά", "Στάλθηκε ✔")

    def run(self):
        self.root.mainloop()
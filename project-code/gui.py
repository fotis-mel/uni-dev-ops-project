import tkinter as tk
from mechanic_gui import MechanicGUI
from tkinter import simpledialog, messagebox


class AppGUI:
    def __init__(self, management):
        self.mgmt = management
        self.root = tk.Tk()
        self.root.title("Login Screen")
        self.root.geometry("500x400")

        tk.Button(self.root, text="Mechanics", command=self.show_mechanics).pack(pady=10)
        tk.Button(self.root, text="Customers", command=self.show_customers).pack(pady=10)
        tk.Button(self.root, text="Admins", command=self.show_admins).pack(pady=10)

    # ----------------------------
    # WINDOW WITH CHECKBOXES
    # ----------------------------
    def open_checkbox_window(self, title, data, role):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("400x400")

        self.selected_vars = []

        for user in data:
            var = tk.BooleanVar()
            name = user.get("full_name", "Unknown")

            tk.Checkbutton(win, text=name, variable=var).pack(anchor="w")
            self.selected_vars.append((name, var))

        # CONFIRM BUTTON
        tk.Button(
            win,
            text="Επιβεβαίωση",
            command=lambda w=win: self.ask_password(role, w)
        ).pack(pady=10)

    # ----------------------------
    # STEP 2: ASK PASSWORD
    # ----------------------------
    def ask_password(self, role, window):
        selected = [name for name, var in self.selected_vars if var.get()]

        if not selected:
            messagebox.showwarning("Warning", "Δεν έχεις επιλέξει χρήστη")
            return

        password = simpledialog.askstring("Password", "Εισάγετε κωδικό:")

        if password is None:
            return

        ok = self.mgmt.validate_user_password(role, selected, password)

        selected_user = selected[0]   # ✔ ΚΛΕΙΔΩΣΕ ΤΟ ΕΔΩ (IMPORTANT)

        if ok:
            window.destroy()

            self.root.after(
                50,
                lambda user=selected_user: self._launch_mechanic(user)
            )
        else:
            messagebox.showerror("Error", "Λάθος κωδικός ❌")
            window.destroy()


    def _open_dashboard(self, window, user):
        try:
            window.destroy()
        except:
            pass

        self.root.after(50, lambda: self._launch_mechanic(user))


    def _launch_mechanic(self, user):
        from mechanic_gui import MechanicGUI
        MechanicGUI(self.mgmt, user, self.root)

    def show_mechanics(self):
            self.open_checkbox_window("Μηχανικοί", self.mgmt.mechanics, "mechanic")

    def show_customers(self):
        self.open_checkbox_window("Πελάτες", self.mgmt.customers, "customer")

    def show_admins(self):
        self.open_checkbox_window("Admins", self.mgmt.admins, "admin")

    def run(self):
        self.root.mainloop()

    
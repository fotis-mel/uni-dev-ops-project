import pandas as pd


class Management:
    def __init__(self):
        self.users_df = None

        self.mechanics = []
        self.customers = []
        self.admins = []

        self.shifts = []
        self.temporary_vehicles = []
        self.scheduled_appointments = []
        self.parts = []

    # ----------------------------
    # CSV USERS
    # ----------------------------
    def load_users(self, csv_path):
        self.users_df = pd.read_csv(csv_path)
        self.split_users_by_role()

    def split_users_by_role(self):
        self.mechanics = self._get_role("mechanic")
        self.customers = self._get_role("customer")
        self.admins = self._get_role("admin")

    def _get_role(self, role):
        return (
            self.users_df[self.users_df["role"] == role]
            .drop(columns=["role"])
            .to_dict("records")
        )

    # ----------------------------
    # PARTS
    # ----------------------------
    def add_part(self, name, quantity, price=None):
        self.parts.append({
            "name": name,
            "quantity": quantity,
            "price": price
        })

    def get_parts(self):
        return self.parts

    # ----------------------------
    # VEHICLES
    # ----------------------------
    def add_vehicle(self, vehicle):
        self.temporary_vehicles.append(vehicle)

    def get_vehicles(self):
        return self.temporary_vehicles

    # ----------------------------
    # SHIFTS
    # ----------------------------
    def add_shift(self, shift):
        self.shifts.append(shift)

    def get_shifts(self):
        return self.shifts

    # ----------------------------
    # APPOINTMENTS
    # ----------------------------
    def schedule_appointment(self, appointment):
        self.scheduled_appointments.append(appointment)

    def get_appointments(self):
        return self.scheduled_appointments

    # ----------------------------
    # UI HELP (format)
    # ----------------------------
    def format_users(self, data):
        if not data:
            return "No data"

        result = ""
        for item in data:
            result += "----------------------\n"
            for k, v in item.items():
                result += f"{k}: {v}\n"
            result += "\n"

        return result

    def validate_user_password(self, role, selected_names, password):

        if role == "mechanic":
            data = self.mechanics
        elif role == "customer":
            data = self.customers
        elif role == "admin":
            data = self.admins
        else:
            return False

        for user in data:
            if user.get("full_name") in selected_names:
                if str(user.get("password")) == str(password):
                    return True

        return False

    def get_user_by_name(self, role, name):
        data = self.mechanics if role == "mechanic" else []

        for u in data:
            if u.get("full_name") == name:
                return u

        return None
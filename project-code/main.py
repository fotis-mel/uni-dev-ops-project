from management import Management
from gui import AppGUI


if __name__ == "__main__":
    mgmt = Management()

    mgmt.load_users("users.csv")

    app = AppGUI(mgmt)
    app.run()
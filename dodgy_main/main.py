# 4PINT Assessment 2 - Paul Stuart 000389223
# Main Controller start application from this file
# 16.06.21

from login import Login as New_login
from dodgy_gui import dodgy_bros as New_dodgy


def main():
    New_login.login_gui()
    if New_login.is_correct_cred():
        New_dodgy.dodgy_interface()


main()

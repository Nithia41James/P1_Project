import os
import getpass
from pyfiglet import figlet_format
from termcolor import colored
from registration import add_user
from src.interface import UserInterface


os.system('cls')
def main():
    ui = UserInterface()
    print("\n\n")
    word = figlet_format("                                  WELCOME  TO  MY  STORE",width = 300)
    print(colored(word,"cyan")) 

    print('*' * 160)
    add_user()
    print("Please login to continue\n")
    username = input("Username: ")
    #password = input("Password: ")
    password = getpass.getpass()
    print(password)

    user = ui.user_act.login(username, password)

    if user:
        if user.username == 'admin':
            ui.title("Welcome Admin")
            ui.admin_ui()
        else:
            ui.title('WELCOME %s' % username)
            ui.user_act.username = username
            ui.user_act.get_user_id()
            # start ui
            ui.user_ui()
    else:
        print("Invalid login, please try again")




if __name__ == "__main__":
    main()
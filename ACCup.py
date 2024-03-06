import random

user_pass = {}

def sign_up():
    global user_pass
    if not user_pass:
        while True:
            username = input("Enter a username: ")
            if username.strip():
                break
            else:
                print("Username cannot be empty. Please try again.")
    
        while True:
            password = input("Enter a password: ")
            if len(password) >= 6:
                re_password = input("Re-enter your password to confirm: ")
                if password == re_password:
                    print('Signed up')
                    user_pass[username] = password
                    break
                else:
                    print("You entered the wrong confirmation password. Please try again.")
            else:
                print("Password should be at least 6 characters long. Please try again.")
    
    else:
        while True:
            username = input("Enter a username: ")
            if username.strip():
                break
            else:
                print("Username cannot be empty. Please try again.")
    
        while True:
            password = input("Enter a password: ")
            if len(password) >= 6:
                re_password = input("Re-enter your password to confirm: ")
                if password == re_password:
                    print('Signed up')
                    user_pass[username] = password
                    break
                else:
                    print("You entered the wrong confirmation password. Please try again.")
            else:
                print("Password should be at least 6 characters long. Please try again.")

def login(system):
    while True:
        username1 = input("Enter your username: ")
        if username1 in system.keys():
            print("Now enter your password:")
            password1 = input("Password: ")
            if password1 == system[username1]:
                print("Logged in")
                break
            else:
                print("Wrong password. Please try again.")
        else:
            print("Wrong username. Please try again.")
            
def psw(reset):
    if not reset:
        print("No users to reset password.")
        return
    
    words = ["fLm0Oj", "bgLp90", "a346Jk", "j9mLIon", "kQz56i"]
    correct_word = random.choice(words)
    print("Please type the word:", correct_word)
    user_input = input("Enter the word: ")
    
    if user_input == correct_word:
        print("You're not a robot.")
        username3 = input("Enter your username: ")
        if username3 in reset:
            while True:
                password3 = input("Enter a new password: ")
                if len(password3) >= 6:
                    if password3 != reset[username3]:
                        re_password1 = input("Re-enter your password to confirm: ")
                        if password3 == re_password1:
                            reset[username3] = password3
                            print("Password reset successfully.")
                            break
                        else:
                            print("You entered the wrong confirmation password. Please try again.")
                    else:
                        print("Your new password must be different from the old one.")
                else:
                    print("Password must be at least 6 characters long.")
        else:
            print("Username not found. Can't reset password.")
    else:
        print("CAPTCHA failed! You might be a robot.")

while True:
    print("Choice\n 1. To sign Up\n 2. To login\n 3. To reset password\n 4. To Exit")
    choose = input("Choose 1, 2, 3, or 4: ")
    if choose == "1":
        sign_up()
    elif choose == "2":
        if user_pass:
            login(user_pass)
        else:
            print("You need to sign up first.")
    elif choose == "3":
        psw(user_pass)
    elif choose == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice. Please choose again.")
# Password reset program
# Only accept a new password if it is:
# 1. At least eight characters long
# 2. Has lower case and upper case letters.
# The password reset program should also make the user input their new password twice so that the computer knows that the user has not made any mistakes when typing their new password.
# Extensions:
# 1. Make some sort of algorithm to suggest how strong the password is (Weak, Medium, Strong) depending on length, whether or not the password has special characters in etc
# 2. Let the user input their username. The program should go to a text file with a list of usernames and old passwords, and the program should only let you change your password if
# you input your old password.

import json, pickle

def isMixed(text):
    if not (text.isdigit and text.islower() and text.isupper()): return True
    else: return False

userFileLocation = "./codeChallenges/passwordReset/pwords.txt"


class user:
    def __init__(self, name, cPword, oPwords):
        self.name = name
        self.cPword = cPword
        self.oPwords = oPwords

    def changePasword(self):
        attempts = 3
        while True:
            gCPword = input("To change you passowrd please type your current password:\n")
            if gCPword == self.cPword:
                attempts = 3
                while True:
                    if attempts == 0: break
                    gNPword = input("Please type your new password:\n")
                    if len(gNPword)>8 and isMixed(gNPword):
                        gRNpword = input("Please retype your new password:\n")
                        if gRNpword == gNPword:
                            self.oPwords.insert(0,self.cPword)
                            self.cPword = gNPword
                            print("Password Successfully Changed")
                            break
                        else:
                            print("That is not the same password")
                    attempts -= 1
            else:
                print("Incorrect Password, Try again")
                attempts -= 1
            break

    def login(self):
        attempts = 3
        while True:
            gPword = input("Please type your password to log in:\n")
            if gPword == self.cPword:
                print("Successfully Logged In \n \n ")
                break
            else:
                if attempts != 0:
                    print("Password Incorrect, Try again, You have: ", attempts, "remaining.")
                    continue
                else:
                    print("Login Failed, Too many failed attempts")
                    break
        input("Press enter to continue\n")
        

                        



admin = user("Admin","administrator",[])
normal = user("normal","normalguy",[])
with open("data","wb") as f:
    pickle.dump(admin,f)
    pickle.dump(normal,f)

with open("data", 'rb') as f:
    data = pickle.load(f)
print(data.cPword)
exit()
while True:
    print("Choose an option \n1. Log In\n2. New User\n3. Change Password")
    option = input()
    if option == "1":
        uname = input("Please Type Username:\n")
        
    
    elif option == "2":
        uname = input("Please type the unsername for your account")    
        

            

    
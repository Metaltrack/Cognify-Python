max_len = 8

def check_pass(pwd :str):
    strength :int = 0

    if len(pwd) >= max_len:
        print("good length")
        strength += 1
    if any(char.isupper() for char in pwd):
        print("has capital")
        strength += 1
    if any(char.islower() for char in pwd):
        print("has lower letter")
        strength += 1
    if any(not c.isalnum() for c in pwd):
        print("has special char")
        strength += 1
        
    print("Strength of password: ", strength)
    if(strength == 0):
        print("Really bad password...")
    elif(strength == 1):
        print("Bad password...")
    elif(strength == 2):
        print("Ok'ish password...")
    elif(strength == 3):
        print("Good password")
    elif(strength == 4):
        print("Perfect password!")
    else:
        print("Something happened (it was not supposed to happen)")

if __name__ == "__main__":
    while(True):
        print("""Level 2 Password Strength...
                    press [1] to check password.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            pwd = str(input("Enter Password: "))
            check_pass(pwd)
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
            

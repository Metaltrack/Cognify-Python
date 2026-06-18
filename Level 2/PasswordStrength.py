import re

def check_pass(pwd :str):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        
    

if __name__ == "__main__":
    while(True):
        print("""Level 2 Password Strength...
                    press [1] to check password.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            pwd = str(input("Enter Password: "))
            
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
            

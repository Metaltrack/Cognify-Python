import re

def verify_mail(email :str):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        
    if re.match(regex, email):
        return True
    else:
        return False

if __name__ == "__main__":
    while(True):
        print("""Level 1 Temperature Conversion...
                    press [1] to check email.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            mail = str(input("Enter Email: "))
            if(verify_mail(mail)):
                print("Email is correct...")
            else:
                print("Email is incorrect...")
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
            

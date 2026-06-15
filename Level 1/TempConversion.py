def CtoF(temp :float):
    return (temp * (9.0/5.0)) + 32

def FtoC(temp :float):
    return (temp - 32) * (5.0/9.0)

def CtoK(temp :float):
    return temp + 273.15

def KtoC(temp :float):
    return temp - 273.15


if __name__ == "__main__":
    while(True):
        print("""Level 1 Temperature Conversion...
                    press [1] to Convert Celsius to Farenheit.
                    press [2] to Convert Farenheit to Celsius.
                    press [3] to Convert Celsius to Kelvin.
                    press [4] to Convert Kelvin to Celsius.
                    press [5] to Convert Farenheit to Kelvin.
                    press [6] to Convert Kelvin to Farenheit.
                    press [7] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            temp = float(input("Enter Temperature-> "))
            print("Temperature converion: ", CtoF(temp))
        elif(choice == 2):
            temp = float(input("Enter Temperature-> "))
            print("Temperature converion: ", FtoC(temp))
        elif(choice == 3):
            temp = float(input("Enter Temperature-> "))
            print("Temperature converion: ", CtoK(temp))
        elif(choice == 4):
            temp = float(input("Enter Temperature-> "))
            print("Temperature converion: ", KtoC(temp))
        elif(choice == 5):
            temp = float(input("Enter Temperature-> "))
            print("Temperature converion: ", CtoK(FtoC(temp)))
        elif(choice == 6):
            temp = float(input("Enter Temperature-> "))
            print("Temperature converion: ", CtoF(KtoC(temp)))
        elif(choice == 7):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
            

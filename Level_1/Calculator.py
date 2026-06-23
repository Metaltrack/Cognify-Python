def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        return "Error cannot divide by zero"
    return a / b

def mul(a, b):
    return a * b

def mod(a, b):
    return a % b

if __name__ == "__main__":
    while(True):
        print("""Level 1 Calculator...
                    press [1] to add.
                    press [2] to sub.
                    press [3] to mul.
                    press [4] to div.
                    press [5] to mod.
                    press [6] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            a = float(input("A: "))
            b = float(input("B: "))
            print("result: ", add(a, b))
        elif(choice == 2):
            a = float(input("A: "))
            b = float(input("B: "))
            print("result: ", sub(a, b))
        elif(choice == 3):
            a = float(input("A: "))
            b = float(input("B: "))
            print("result: ", mul(a, b))
        elif(choice == 4):
            a = float(input("A: "))
            b = float(input("B: "))
            print("result: ", div(a, b))
        elif(choice == 5):
            a = float(input("A: "))
            b = float(input("B: "))
            print("result: ", mod(a, b))
        elif(choice == 6):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue

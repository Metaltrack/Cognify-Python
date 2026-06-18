def generate_sequence(max_len :int):
    a :int = 0
    b :int = 1
    c :int = a + b

    print("Sequence: ")
    print(a)
    print(b)
    print(c)

    for i in range(2, max_len - 1):
        a = b
        b = c
        c = a + b
        print(c)

if __name__ == "__main__":
    while(True):
        print("""Level 2 Fibonacci...
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            num = int(input("Enter max length: "))
            generate_sequence(num)
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue
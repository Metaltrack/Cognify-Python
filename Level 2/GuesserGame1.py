from random import randint

num_to_guess :int

def generate_number():
    return randint(1, 100)

def check_number(number :int, guess :int):
    accurracy = (abs(100 - abs(number - guess)) / 100)
    if accurracy == 1.0:
        return "ABSOLUTELY CORECT!!!! YOU GOT IT :)"
    target = "lower" if guess < number else "higher"
    return f"you guessed {guess}, which is {accurracy * 100}% accurate, you are still {target}"

if __name__ == "__main__":
    while(True):
        print("""Level 2 Guesser-Game-1..
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            num_to_guess = generate_number()
            print("The device has chosen!")
            while True:
                num = int(input("Enter your guess: "))
                print(check_number(num_to_guess, num))
                if num == num_to_guess:
                    break
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue

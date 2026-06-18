from random import randint

num_to_guess :int

def generate_number(r :list[int]):
    return randint(r[0], r[1])

def check_number(number :int, guess :int, r :list[int]):
    accurracy = (abs(r[1] - abs(number - guess)) / r[1])
    if accurracy == 1.0:
        return "ABSOLUTELY CORECT!!!! YOU GOT IT :)"
    target = "lower" if guess < number else "higher"
    return f"you guessed {guess}, which is {accurracy * 100}% accurate, you are still {target}"

if __name__ == "__main__":
    while(True):
        print("""Level 2 Guesser-Game-2...
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            print("Enter the range of numbers...")
            num1 = int(input("Minimum number: "))
            num2 = int(input("Maximum number: "))
            num_to_guess = generate_number([num1, num2])
            print("The device has chosen!")
            while True:
                num = int(input("Enter your guess: "))
                print(check_number(num_to_guess, num, [num1, num2]))
                if num == num_to_guess:
                    break
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue


#this is here because I run these files directly as a command in main program
#but then .StringReversal (which looks for local implementation) does not work
#if I remove it and import normally then main program fails as this file is an import there
try:
    from .StringReversal import string_reversal_slice
except ImportError:
    from StringReversal import string_reversal_slice

def check_palindrome(word :str):
    r_word = string_reversal_slice(word)
    if word == r_word:
        return True
    return False

if __name__ == "__main__":
    while(True):
        print("""Level 1 Palindrome...
                    press [1] to check palindrome.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            word = str(input("Enter word: "))
            if check_palindrome(word):
                print(f"Word {word} is a palindrome")
            else:
                print(f"Word {word} is NOT a palindrome")
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue

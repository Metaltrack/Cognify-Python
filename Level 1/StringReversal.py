#Basic string reversal, reversed(str) gives an object which is then joined to the empty ''
#the reversed(str) function gives the iterator to the end of the string which is used by the join function
#which iterates over it normally (but our iterator itself is in reverse order)

from encodings.punycode import insertion_unsort


def string_reversal_join(in_string :str):
    return ''.join(reversed(in_string))


#In string slice the slice notation is given as [start:stop:step]
#to step backwards (which will get us reverse string) we just do -1
def string_reversal_slice(in_string :str):
    return in_string[::-1]


#gonna start with i as our iterator set to the length of string "hello" = 5
#string array will be 0,1,2,3,4 but i starts at 5 so we do i-1
# check till i >= 0 and return the final string
def string_reversal_loop(in_string :str):
    new_string :str = ""
    
    i = len(in_string) - 1
    while i >= 0:
        new_string += in_string[i]
        i -= 1

    return new_string

if __name__ == "__main__":
    while(True):
        print("""Level 1 String Reversal...
                    press [1] to reverse using string operations.
                    press [2] to reverse using string slices.
                    press [3] to reverse using loop.
                    press [4] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            string = str(input("Enter string-> "))
            print(string_reversal_join(string))
        elif(choice == 2):
            string = str(input("Enter string-> "))
            print(string_reversal_slice(string))
        elif(choice == 3):
            string = str(input("Enter string-> "))
            print(string_reversal_loop(string))
        elif(choice == 4):
            print("exiting...")
            break
        else:
            print("Invalid input!")
            continue
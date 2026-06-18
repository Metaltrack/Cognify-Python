import os
import string

word_data = {}

def load_file(path :str):
    with open(path, "r") as file:
        return file.read().lower()

def main_stuff(data :str):
    for char in string.punctuation:
        data = data.replace(char, " ")

    words = data.split()

    for word in words:
        if word in word_data:
            word_data[word] += 1
        else:
            word_data[word] = 1

    print("Word Occurrences:\n")
    for word in sorted(word_data.keys()):
        print(f"{word}: \t{word_data[word]}")

if __name__ == "__main__":
    while(True):
        print("""Level 2 File Manipulation...
                    press [1] to start.
                    press [2] to exit.
        """)
        choice = int(input("Choice: "))

        if(choice == 1):
            path = str(input("Enter file path (press enter to give default path): "))
            if path:
                main_stuff(load_file(path))
            else:
                directory = os.path.dirname(os.path.realpath(__file__))
                file_path = directory + "\\file_to_be_manipulated.txt"
                print("Reverting to default path: ", file_path)
                main_stuff(load_file(file_path))
        elif(choice == 2):
            print("exiting...")
            break
        else:
            print("Invalid Input!")
            continue

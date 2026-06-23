from Level_1 import Calculator, EmailValidator, Palindrome, StringReversal, TempConversion
from Level_2 import Fibonacci, FileManipulation, GuesserGame1, GuesserGame2, PasswordStrength
from Level_3 import Automation, DataPlotting, WebScraper
import os
import subprocess

level_1_path = os.path.dirname(__file__) + "\Level_1"
level_2_path = os.path.dirname(__file__) + "\Level_2"
level_3_path = os.path.dirname(__file__) + "\Level_3"


if __name__ == "__main__":
    while True:
        print("""
             ██████╗ ██████╗  ██████╗ ███╗   ██╗██╗███████╗██╗   ██╗
            ██╔════╝██╔═══██╗██╔════╝ ████╗  ██║██║██╔════╝╚██╗ ██╔╝
            ██║     ██║   ██║██║  ███╗██╔██╗ ██║██║█████╗   ╚████╔╝ 
            ██║     ██║   ██║██║   ██║██║╚██╗██║██║██╔══╝    ╚██╔╝  
            ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║██║██║        ██║   
             ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝        ╚═╝   
        """)
        print("""
        ╦ ╦┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ┌┬┐┬ ┬┌─┐  ┌┬┐┌─┐┬┌┐┌  ┌─┐┬─┐┌─┐┌─┐┬─┐┌─┐┌┬┐   
        ║║║├┤ │  │  │ ││││├┤    │ │ │   │ ├─┤├┤   │││├─┤││││  ├─┘├┬┘│ ││ ┬├┬┘├─┤│││   
        ╚╩╝└─┘┴─┘└─┘└─┘┴ ┴└─┘   ┴ └─┘   ┴ ┴ ┴└─┘  ┴ ┴┴ ┴┴┘└┘  ┴  ┴└─└─┘└─┘┴└─┴ ┴┴ ┴ooo
        """)
        level = int(input("Input Level {Level 1, 2, 3}: "))

        if level == 1:
            files = []
            for file in os.listdir(level_1_path):
                if file.lower().endswith(".py"):
                    files.append(file)
            

            print("""
                                                           _       _               
            \    / _  |  _  _  ._ _   _     _|_  _     |  |_ \  / |_ |     /|      
             \/\/ (/_ | (_ (_) | | | (/_     |_ (_)    |_ |_  \/  |_ |_     | o o o
            """)

            print(f"Total {len(files)} files found...")
            for i in range(len(files)):
                print(f"{i}>>{files[i]}")

            choice = int(input("Choose file to run [num]: "))

            subprocess.Popen(
                ['cmd', '/c', 'start', 'cmd', '/k', 'python', level_1_path + "\\" + files[choice]],
                shell=True
            )
        elif level == 2:
            files = []
            for file in os.listdir(level_2_path):
                if file.lower().endswith(".py"):
                    files.append(file)
            

            print("""
                                                               _       _       _       
                \    / _  |  _  _  ._ _   _     _|_  _     |  |_ \  / |_ |      )      
                 \/\/ (/_ | (_ (_) | | | (/_     |_ (_)    |_ |_  \/  |_ |_    /_ o o o
            """)

            print(f"Total {len(files)} files found...")
            for i in range(len(files)):
                print(f"{i}>>{files[i]}")

            choice = int(input("Choose file to run [num]: "))

            subprocess.Popen(
                ['cmd', '/c', 'start', 'cmd', '/k', 'python', level_2_path + "\\" + files[choice]],
                shell=True
            )
        elif level == 3:
            files = []
            for file in os.listdir(level_3_path):
                if file.lower().endswith(".py"):
                    files.append(file)
            

            print("""
                                                               _       _       _       
                \    / _  |  _  _  ._ _   _     _|_  _     |  |_ \  / |_ |     _)      
                 \/\/ (/_ | (_ (_) | | | (/_     |_ (_)    |_ |_  \/  |_ |_    _) o o o
            """)

            print(f"Total {len(files)} files found...")
            for i in range(len(files)):
                print(f"{i}>>{files[i]}")

            choice = int(input("Choose file to run [num]: "))

            subprocess.Popen(
                ['cmd', '/c', 'start', 'cmd', '/k', 'python', level_3_path + "\\" + files[choice]],
                shell=True
            )
        else:
            print("\nInvalid Input... try again\n\n")

        
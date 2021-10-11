import Task3.task3 as t3
import Task2.task2 as t2
import Task1.task1 as t1



def main():
    message = "\n\n= CZ3005 Lab 1 Project Main Menu =\n\
    = Description = \n\
    Algorithm 1 - Shortest Distance without Energy Constraint\n\
    Algorithm 2 - Shortest Distance with Energy Constraint using USC\n\
    Algorithm 3 - Shortest Distance with Energy Constraint using ASTAR\n\n\
    == Presets - Start Node: 1, Target Node: 50, Energy Budget: 287932 == \n\
    1) Algorithm 1 [Preset]\n\
    2) Algorithm 2 [Preset]\n\
    3) Algorithm 3 [Preset]\n\n\
    == Manual - Enter your own nodes and energy budget ==\n\
    4) Algorithm 1 [Manual]\n\
    5) Algorithm 2 [Manual]\n\
    6) Algorithm 3 [Manual]\n\n\
    7) Quit\n"
   

    quit = False
    while (not(quit)):

        print(message)

        try:
            choice = int(input("Please enter your choice: "))

            if (choice == 1):
                print("Running Algorithm 1 - Preset\n")
                t1.main()
                input("Press [Enter] to continue...")
            elif (choice == 2):
                print("Running Algorithm 2 - Preset\n")
                t2.main()
                input("Press [Enter] to continue...")
            elif (choice == 3):
                print("Running Algorithm 3 - Preset\n")
                t3.main_preset()
                input("Press [Enter] to continue...")
            elif (choice == 4):
                print("Running Algorithm 1 - Manual\n")
                t1.custom()
                input("Press [Enter] to continue...")
            elif (choice == 5):
                print("Running Algorithm 2 - Manual\n")
                t2.custom()
                input("Press [Enter] to continue...")
            elif (choice == 6):
                print("Running Algorithm 3 - Manual\n")
                t3.main_manual()
                input("Press [Enter] to continue...")
            
            elif (choice == 7):
                quit = True
                print("Quiting...\n")
            else:
                print("Invalid choice! Please try again")

        except:
            print("Please enter a number!")

if __name__ == "__main__":
    main()


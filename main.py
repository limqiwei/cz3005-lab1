import Task3.task3 as t3
import Task2.task2 as t2
import Task1.task1 as t1



def main():
    message = "= CZ3005 Lab 1 Project Main Menu =\n\
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
    7) Quit)"

    print(message)
    

    quit = False
    while (not(quit)):
        try:
            choice = int(input("Please enter your choice: "))
            if (choice == 1):
                print("Running Algorith 1 - Preset")
                t1.main()
            elif (choice == 2):
                print("Running Algorith 2 - Preset")
                t2.main()
            elif (choice == 3):
                print("Running Algorith 3 - Preset")
                t3.main()
            elif (choice == 4):
                print("Running Algorith 1 - Manual")
                # Call function here
            elif (choice == 5):
                print("Running Algorith 2 - Manual")
                # Call function here
            elif (choice == 6):
                print("Running Algorith 3 - Manual")
                # Call function here
            elif (choice == 7):
                quit = True
                print("Quiting...")
            else:
                print("Invalid choice! Please try again")
        except:
            print("Please enter a number!")

if __name__ == "__main__":
    main()



    
    




    



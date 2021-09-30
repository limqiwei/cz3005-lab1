import Task3.task3 as t3
import Task2.task2 as t2
import Task1.task1 as t1



def main():
    message = "== Main Menu ==\n\
        1) Algorithm 1 - Shortest Distance\n\
        2) Algorithm 2 - Shortest Distance with Energy Constraint using USC\n\
        3) Algorithm 3 - Shortest Distance with Energy Constraint using ASTAR\n\
        4) Quit)"
    print(message)
    

    quit = False
    while (not(quit)):
        try:
            choice = int(input("Please enter your choice: "))
            if (choice == 1):
                t1.main()
            elif (choice == 2):
                t2.main()
            elif (choice ==3):
                t3.main()
            elif (choice ==4):
                quit = True
                print("Quiting...")
            else:
                print("Invalid choice! Please try again")
                print(message)
        except:
            print(message)
            print("Please enter a number!")

if __name__ == "__main__":
    main()



    
    




    



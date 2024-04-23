tasks = []
pointTracker = []
totalPoints = 0

def addTask():
    task = input("Please enter a task: ")
    points = int(input("How many points is this worth: "))
    tasks.append(task)
    pointTracker.append(points)

    print(f"Task '{task}' added to the list and is worth {points} points!")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")

        for (task, points) in zip(tasks, pointTracker):
            print(f"{task} worth {points} points!")

def deleteTask():
    listTasks()

    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            pointTracker.pop(taskToDelete)

        else:
            print(f"Task #{taskToDelete} was not found")

    except:
        print("Invalid input.")

def completeTask():
    listTasks()

    try:
        taskToComplete = int(input("Enter the # to complete: "))
        if taskToComplete >= 0 and taskToComplete < len(tasks):
            global totalPoints 
            totalPoints += pointTracker[taskToComplete]
            tasks.pop(taskToComplete)
            pointTracker.pop(taskToComplete)

        else:
            print(f"Task #{taskToComplete} was not found")

    except:
       print("Invalid input.")

def storePage():
    global totalPoints
    while True:
        print("\n")
        print("*****--------------------------------*****")
        print("Welcome to the store!")
        print(f"You currently have {totalPoints} points, hopefully you have enough for something!")
        print("*****--------------------------------*****")
        print("\n")

        print("1. Read for an hour       || 10 points")
        print("2. Go out for fast food   || 50 points")
        print("3. Start doomscrolling    || 90 points")
        print("4. Watch a sports game    || 25 points")
        print("5. Binge watch The Office || 20 points")
        print("6. Fight for Democracy    || 05 points")
        print("7. Return to Main Menu    || Free!")
        
        storeChoice = input("Enter your selection: ")

        if (storeChoice == "1"):
            read = 10
            if totalPoints - read < 0:
                print("Sorry, you dont have enough points to do that!")
            else:
                totalPoints -= read
                print("\n")
                print("Have fun reading!")
                print("\n")
        elif (storeChoice == "2"):
            food = 50
            if totalPoints - food < 0:
                print("Sorry, you dont have enough points to do that!")
            else:
                totalPoints -= food
                print("\n")
                print("Enjoy your meal, you earned it!")
                print("\n")
        elif (storeChoice == "3"):
            doom = 90
            if totalPoints - doom < 0:
                print("Sorry, you dont have enough points to do that!")
            else:
                totalPoints -= doom
                print("\n")
                print("See you whenever you get out of the loop.")
                print("\n")
        elif (storeChoice == "4"):
            sports = 25
            if totalPoints - sports < 0:
                print("Sorry, you dont have enough points to do that!")
            else:
                totalPoints -= sports
                print("\n")
                print("May your team win!")
                print("\n")
        elif (storeChoice == "5"):
            office = 20
            if totalPoints - office < 0:
                print("Sorry, you dont have enough points to do that!")
            else:
                totalPoints -= office
                print("\n")
                print("Identity theft is not a joke Jim!")
                print("\n")
        elif (storeChoice == "6"): 
            democracy = 5
            if totalPoints - democracy < 0:
                print("Sorry, you dont have enough points to do that!")
            else:
                totalPoints -= democracy
                print("\n")
                print("For Malevelon Creek!")
                print("\n")                
        elif (storeChoice == "7"): 
            break
        else:
            print("Invalid input, please try again.")

if __name__ == "__main__":

    print("Welcome to Gamify Your Schedule!")
    user = input('Please enter your name: ')
    print(f"Hi there {user}! I hope you enjoy this little demo.")
    while True:
        print("\n")
        print("*****--------------------------------*****")
        print("Please select one of the following options")
        print("*****--------------------------------*****")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Complete a Task")
        print("5. View Points")
        print("6. View Store")
        print("7. Quit")
        
        choice = input("Enter your selection: ")

        print("\n")

        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            completeTask()
        elif (choice == "5"):
            print(f"Your current point total is {totalPoints}.")
        elif (choice == "6"): 
            storePage()
        elif (choice == "7"): 
            break
        else:
            print("Invalid input, please try again.")
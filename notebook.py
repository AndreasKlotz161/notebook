import os
import time
import pickle


def displayTasks():
    os.system("cls") #executes 'cls' in terminal -> 'cls' deletes all lines in terminal
    sortTasks()
    if tasks:
        for number, task in enumerate(tasks, start=1):
            status = "\33[32mdone\33[0m" if task[1] else "\33[31mtodo\33[0m"
            print(f'{number}....{status}.....{task[0]}')
    else:
        print("There are no tasks in the list.")

#sorts tasks by second task index, wich is the value of tasks status
def sortTasks():
    global tasks
    tasks = sorted(tasks, key=lambda x: x[1])

#prompts the user to add a new task and appends it to the tasks list returns True if a task was added when a text was enterd
def addTask():
    os.system("cls")
    taskText = input("Enter your new task or press enter to escape:\n")
    if taskText: #if the user enterd a text(=a new task)
        tasks.append([taskText, False])# add the new task and set its status to false (='todo')
        print(f"\33[33m{taskText}\33[0m added to the list.")
        time.sleep(1)
        return True
    else:#return false if there was nothing enterd by user to break the loop of adding tasks
        return False

#deletes a task by the task number enterd, if nothing was enterd or there are no tasks return false
def deleteTask():
    displayTasks()
    if tasks:#if any task exists
        try:#ask the user for the tasknumber to delete
            taskNumber = input("Enter the number of the task or nothing to escape: ")
            if taskNumber:#if the user enterd osmething try casting it to an integre
                taskNumber = int(taskNumber)
            else:#return False to exit the loop
                return False
            try:# try to delete task at given number
                del tasks[taskNumber-1]
                return True #return True to repeat the loop for deleting a task
            except:#if the task number does not exist
                print(f"There is no task with the number {taskNumber}")
                time.sleep(2)
                return True # retrun True for repeating the loop to delete a task
        except:
            print("You have to enter a number.")
            time.sleep(2)
            return True # retrun True for repeating the loop to delete a task
    else:# if there are no tasks in the list
        time.sleep(2)
        return False

#changes a task status wich can be selected by number. returns False if there are no tasks or nothing was enterd for task
def changeTaskStatus():
    displayTasks()
    if tasks:#if there are tasks in the list
        try: #prompt user input 
            taskNumber = input("Enter the number of the task or nothing to escape: ")
            if taskNumber: #if the user entered something try typcasting to integer
                taskNumber = int(taskNumber)
            else:#if the user entered nothing
                return False
            try:#try to switch status of given tasknumber
                tasks[taskNumber-1][1] = not tasks[taskNumber-1][1]
                return True #retrun True so the loop will begin again
            except:# if the tasknumber does not exist write errormessage and return True to repeat the loop
                print(f"There is no task with the number {taskNumber}")
                time.sleep(2)
                return True
        except:# if the user entered something wich can not be an integer write errormessage and repeat the loop
            print("You have to enter a number.")
            time.sleep(2)
            return True
    else:# if the list is empty return false to break the loop
        time.sleep(2)
        return False
            
#changes the text of a task selected by number of task, returns false if no number was entered or no tasks exists
def changeTaskText():
    displayTasks()#show all tasks
    if tasks: #if there are any
        try: #get an input from user
            taskNumber = input("Enter the number of the task or nothing to escape: ")
            if taskNumber: #if the user enterd something try to cast it to integer
                taskNumber = int(taskNumber)
            else:
                return False #return False if nothing was entered
            try:#try to call that number in tasks
                print(f"Old text: \33[33m{tasks[taskNumber-1][0]}\33[0m")
                tasks[taskNumber-1][0] = input("Enter the new Text for this task:\n")
                print("Text was changed.")
                return True #return True if a task was changed
            except:# if there is no task at enterd number
                print(f"There is no task with the number {taskNumber}")
                time.sleep(2)
                return True
        except:# if the user did not enter a text wich can be an interger
            print("You have to enter a number.")
            time.sleep(2)
            return True
    else:# if there are no tasks in the list
        time.sleep(2)
        return False
    

tasks = []

#try to read saved tasks from file
try:
    tasks = pickle.load(open("notebook/savedTasks.pickle", "rb"))
except:
    print("file not found")

#--------RUN-----------------------------------
while True:
    os.system("cls")
    try: #prompt the user for a number
        task = int(input("""1. Add task 
2. View all tasks
3. Change task status
4. Update task
5. Delete task
6. Quit
-----------------------------
Enter your choice (a number):""").strip())
    except:#if the user has not entered a number
        print("Enter a valid task, tomatohead")
        time.sleep(4)
        continue
    if task == 1:
        while addTask():#runs the function while the user entered something
            {}
    elif task == 2:
        displayTasks()
        input("Press enter to continue...")
    elif task == 3:
        while changeTaskStatus():#runs the function while there are tasks and the user entered something for the number
            {}
    elif task == 4:
        while changeTaskText():#runs the function while there are tasks and the user entered something for the number
            {}
    elif task == 5:
        while deleteTask():#runs the function while there are tasks left and the user entered something for the number
            {}
    elif task == 6: #end program and save tasks in 'savedTasks.pickle' by overwriting
        print("Thanks for using notebook. Your notes will be saved")
        try:
            pickle.dump(tasks, open("notebook/savedTasks.pickle", "wb"))
        except:
            print("file can not be created")
        time.sleep(4)
        os.system("cls")
        break
    else: # if the number entered is not an option from the list
        print("Enter a valid task.")
        time.sleep(2)
        continue
    
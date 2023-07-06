
import os
from datetime import datetime
current_path = os.path.dirname(__file__)

#Declare variables

user_names = []
pass_words = []

#for loop will loop through the lines and append new data to list 
file = open("user.txt","r")
for line in file.readlines():
    Lines = line.strip()
    Lines = Lines.split(", ") 
    user_names.append(Lines[0])
    pass_words.append(Lines[-1])

login = False
while login == False:
     user_name = (input("Please enter a username: "))
     user_pass = (input("Please enter a password: "))

# if above is not true below will be false and message will be printed out 
     if user_name in user_names and user_pass in pass_words:
         
        print(user_name, "has successfully logged in")
        login = True
        break
     else:
        print(" invalid log in details ")
 
# if user selects r username and password will be asked to be enterd.  
# if password is equal to confirm they will be added to user file in user.txt           
def reg_user():
    new_user_login = False
    if menu == "r":
        if user_name == "admin":
            new_user_login = False
            
            while new_user_login == False:
                
                new_username = input("Enter your username : ")
                
                if new_username in user_names:
                    print("UserName is taken")
                else:
                    new_user_login=True
                    
            while new_user_login == True:
                new_user_pass = input("Enter a password:")
                
                check = input("confirm password:")
                if new_user_pass == check:
                    new_user_login = False
                    
                    print(new_username," is offically registered" ) 
                    f = open("user.txt","a")
                    f.write(f"\n{new_username}, {new_user_pass}")
                    f.close()
                else :
                    print("password do not match. try again!")
        else:
            print("only the admin is allowed to add a new user")  
                
# if "a" is selected (tasks.txt) will opend and ask user a set of questions       
# After that the file will close 
def add_task():
    import datetime

    if menu == 'a':
            file = open("tasks.txt","a+")
            Task = input("Enter the username of the asignee: ")
            Title = input("what is the title of your task ?: ")
            Description = input("what does your task do ?: ")
            Due_Date = input("What date is your task due DD-MM-YYYY?: ")
            Date = datetime.datetime.now().date()
            Completed = "No" 
            file.write('\n'+ str(Task) + ", " + str(Title) + ", " + str(Description) + ", " + str(Due_Date) + ", " + str(Date) + ", " + str(Completed))
            file.close()
        
# if "va" is selected All task wll be read in a set format. 
def view_all():
    if menu =="va":
        with open("tasks.txt","r+") as f:
            task_list = []
            for line in f.readlines():
                Lines = line.strip()
                Lines = line.split(",")  
                task_list.append(Lines)

            for task in task_list:
                print("Task asigned to :\t ", task[0])
                print("Title :\t \t \t",task[1])
                print("Description :\t \t", task[2])
                print("Due Date :\t \t", task[3])
                print("Date :\t \t \t", task[4])
                print("Completed ?: \t \t ", task[5])
                    

# if "vm" is selected username enterd in login above is equal to tasks.txt.
# Then the below will only print out the task assigned by tasks.txt
def view_mine():
    user = False
    tasks_files = []
    print("\nView My Tasks")

    #Loop through all the tasks in the list.
    for index in range(0,len(tasks)):
        if user_name == tasks[index][0]:
            tasks_files.append(tasks[index])
            user = True

    #If the user is found, print each task assigned to the current user and add a task number to each task for easy access 
    if user:
        for index in range(0,len(tasks_files)):
            print(f"\n Task {index+1}")
            print("Task:\t \t \t",tasks_files[index][1])
            print("Assigned to:\t \t",tasks_files[index][0])
            print("Date assigned:\t \t",tasks_files[index][3])
            print("Due Date:\t \t",tasks_files[index][4])
            print("Task Completed ?:\t",tasks_files[index][5])
            print("Task Descrption:\t",tasks_files[index][2])
            
        # Ask the user to input the task they wish to edit.
        while True:
            #Add a try / except block in case the user doesn't enter anything so it returns to menu
            try:
                number_of_tasks = int(input("Please enter a task number to edit or press -1 to reurn to menu : "))
                if number_of_tasks == -1:
                   return menu
                
                elif number_of_tasks > 0 and number_of_tasks <= len(tasks_files):
                    
                    #Remove, edit and re add the new task to tasks.txt
                    for index in range(0, len(tasks_files)):
                        tasks.remove(tasks_files[index])

                    #Loop until the user enters a valid option
                    while True:
                        print("\nPlease choose options")
                        print("m - mark task as complete\ne - edit the task")
                        menu_choice = input()

                        #If the user chooses "m", edit the Completed to "Yes".
                        if menu_choice == "m":
                            tasks_files[number_of_tasks-1][5] = "Yes"
                            print(f"\nTask {number_of_tasks } has been marked as complete.")
                            break

                        elif menu_choice == "-1":
                            break

                        #If the user chooses "e", they can edit the Username and Due Date of the task.
                        elif menu_choice == "e":
                            if tasks_files[number_of_tasks-1][5] == "Yes":
                                print("The task has been completed \n.")
                                break
                            else:
                                print("Enter the new Username and Due Date \n ")
                                user_new_edit= input("Edit Username:\t")
                                due_date = input("Edit Due Date:\t")
                                
                             #Check if the users inputs are not blank.
                                if user_new_edit != "":
                                    tasks_files [number_of_tasks-1][0] = user_new_edit
                                if due_date != "":
                                    tasks_files[number_of_tasks-1][4] = due_date

                                print("\n new details")
                                print("Username:\t" + tasks_files[number_of_tasks-1][0])
                                print("Due Date:\t" + tasks_files[number_of_tasks-1][4])
                                break
                        
                        #Let the user know if the input is not recognised
                        else:
                            print("invalid input does not recognize this. \n ")

                    #Add the newly edited tasks in "my_tasks" to "tasks".
                    task.seek(0)
                    task.truncate(0)
                    for index in range(0,len(tasks_files)):
                        tasks.append(tasks_files[index])
                    for index in range(len(tasks)):
                        task.write(", ".join(tasks[index]))
                        if index != len(tasks)-1:
                            task.write("\n")
                    break
                
                #Let the user know if the task entered does not exist.
                else:
                    print("\nThe selected task does not exist. Please try again.\n")
            except:
                print("\nNo task number entered. Please try again.\n")
                
    #Let the user know if they have no tasks.
    if not user:
        print("zero tasks found for selected user.")


#If the user inputs 'ds' statistics are shown
def display_statistics():
    
    #Check if the user is "admin"
    if user_name == "admin":
        
        #Generate reports constantly
        generate_reports()

        # This opens both of the files
        task_over_r = open(os.path.join(current_path, "task_overview.txt"), "r+")
        user_over_r = open(os.path.join(current_path, "user_overview.txt"), "r+")

        #Adjust format
        for line in task_over_r:
            if "Total" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

        for line in user_over_r:
            if "User:" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t\t"))
            elif "User Tasks" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

    #If the user is not "admin" let them know they are not authorised to use this function.
    else:
        print("\n not allowed to view statistics.\n")

#If the user inputs 'gr' reports are generated with statistics about the tasks and each user.
def generate_reports():

    #Check if the logged in user is "admin"
    if user_name == "admin":

        #Open the files and set them to write
        task_over_w = open(os.path.join(current_path, "task_overview.txt"), "w+")
        user_over_w = open(os.path.join(current_path, "user_overview.txt"), "w+")
        
        #Define variables
        total_tasks = len(tasks)
        num_completed = 0
        num_incomplete = 0
        num_inc_overdue = 0
        per_incomplete = 0
        per_overdue = 0

        #Loop through each task and update the variables based on the information for each task.
        for index in range(0, len(tasks)):
            if tasks[index][5] == "Yes":
                num_completed += 1
            elif tasks[index][5] == "No":
                num_incomplete += 1

                #Convert the Due Date to a datetime object and compare the current date to the due date.
                task_date = datetime.strptime(tasks[index][4], '%d - %b - %y')
                if datetime.date(datetime.now()) < task_date.date():
                    num_inc_overdue += 1

        if total_tasks == 0:
            per_incomplete = 0
            per_overdue = 0
        else:
            per_incomplete = round(100*num_incomplete/total_tasks)
            per_overdue = round(100*num_inc_overdue/total_tasks)

        #Write the statistics to the files.
        task_over_w.write(" Task Overview \n\n")
        task_over_w.write(f"Total Tasks:\t\t{total_tasks}\nCompleted Tasks:\t{num_completed}\nIncomplete Tasks:\t{num_incomplete}\nOverdue Tasks:\t\t{num_inc_overdue}\nPortion Incomplete:\t{per_incomplete}%\nPortion Overdue:\t{per_overdue}%")

        number_of_users = len(users)
        user_over_w.write("User Overview \n\n")
        user_over_w.write(f"Total Users:\t\t{number_of_users}\n")
        user_over_w.write(f"Total Tasks:\t\t{total_tasks}")

        # This resets the variables for each user
        for index in range(0, len(users)):
            number_of_tasks = 0
            number_of_completed = 0
            number_of_incomplete = 0
            number_of_inc_overdue = 0
            per_incomplete = 0
            per_overdue = 0
            per_completed = 0
            por_tasks = 0
            
            user_over_w.write("\n----------------------------------------------------\n")
            user_over_w.write(f"User:\t\t\t\t\t{users[index][0]}\n")
            
            # will Loop through each of the tasks
            # This Checks if the task is assigned to the current user
            for assigned in range(0, len(tasks)):

                
                if users[index][0] == tasks[assigned][0]:
                    number_of_tasks +=1
                    if tasks[assigned][5] == "Yes":
                        number_of_completed += 1
                    elif tasks[assigned][5] == "No":
                        number_of_incomplete += 1
                        task_date = datetime.strptime(tasks[assigned][-3], '%d-%b-%y')
                        if datetime.date(datetime.now()) < task_date.date():
                            number_of_inc_overdue += 1

            if number_of_tasks == 0:
                per_incomplete = 0
                per_overdue = 0
                per_completed = 0
            else:
                per_incomplete = round(100*num_incomplete/number_of_tasks)
                per_overdue = round(100*num_inc_overdue/number_of_tasks)
                per_completed = round(100*num_completed/number_of_tasks)

            if total_tasks == 0:
                por_tasks = 0
            else:
                por_tasks = round(100*number_of_tasks/total_tasks)

            #Writes the info to the file
            user_over_w.write(f"User Tasks:\t\t\t\t{number_of_tasks}\nPortion Total Tasks:\t{por_tasks}%\nPortion Completed:\t\t{per_completed}%\nPortion Incomplete:\t\t{per_incomplete}%\nPortion Overdue:\t\t{per_overdue}%")
            user_over_w.write("\n----------------------------------------------------\n")
        
        
        #Closes both files
        print(" Reports has been created: task_overview.txt and user_overview.txt \n")
        task_over_w.close()
        user_over_w.close()
    

# This Loop t will run until the user exits
while True:

    #Open the text files and read the contents into a list variable.
    user = open(os.path.join(current_path, "user.txt"), "r+")
    users = user.readlines()
    users = [index.strip().split(", ") for index in users]

    task = open(os.path.join(current_path, "tasks.txt"), "r+")
    tasks = task.readlines()
    tasks = [index.strip().split(", ") for index in tasks] 

# will continue to run as the condition is met
    if user_name == "admin":
        print(" select one of the following options: \n ")
        print("r - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit")
        menu = input("")
    else:
        print("select one of the following options: \n ")
        print("a - add task\nva - view all tasks\nvm - view my tasks\ne - exit")
        menu = input("")
    
    # program will run based on the users input
    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()
        
    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "ds":
        display_statistics()

    elif menu == "gr":
        generate_reports()

    # the user inputs 'e' the loop is stopped and the program closes.
    elif menu == "e":
        print("Goodbye")
        break

    #the input the user has entered is not recognised the user starts again.
    else:
        print("Invalid input. Please retry.\n ")

    #close files
    user.close()
    task.close()
    
# copied and paste some part of my capstone 19 in This code 
# mayed use of stackflow
# I also got ideas from discord which also helped 
# w3 schools as well  
    
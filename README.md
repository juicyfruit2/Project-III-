# Compulsory Task 1 - README

This project is an enhancement of the previous Capstone project (task_manager.py) with added functionality and improved code modularity using functions. The goal is to create a task management program that allows users to register, add tasks, and view task information.

## Table of Contents

1. [Project Setup](#project-setup)
2. [Functionality](#functionality)
   - [Registering a User](#registering-a-user)
   - [Adding a Task](#adding-a-task)
   - [Viewing All Tasks](#viewing-all-tasks)
   - [Viewing User's Assigned Tasks](#viewing-users-assigned-tasks)
   - [Editing Tasks](#editing-tasks)
   - [Generating Reports](#generating-reports)
   - [Displaying Statistics](#displaying-statistics)
3. [Contact](#contact)

## Project Setup <a name="project-setup"></a>

To get started with this project, follow these steps:

1. Make a copy of the previous Capstone project (task_manager.py) and save it in the Dropbox folder for this project.
2. Copy and paste the text files (user.txt and tasks.txt) that accompanied the previous Capstone project to the Dropbox folder for this project.
3. Modify the code of the copied project to incorporate the new functionalities outlined below.

## Functionality <a name="functionality"></a>

The modified project includes the following functions:

### Registering a User <a name="registering-a-user"></a>

- The function `reg_user()` is called when the user selects 'r' to register a user.
- It ensures that duplicate usernames are not added to user.txt.
- If a duplicate username is entered, an error message is displayed, and the user is allowed to try again with a different username.

### Adding a Task <a name="adding-a-task"></a>

- The function `add_task()` is called when the user selects 'a' to add a new task.
- It prompts the user for task details such as the task name, description, assigned user, and due date.
- The new task is saved in the tasks.txt file.

### Viewing All Tasks <a name="viewing-all-tasks"></a>

- The function `view_all()` is called when users type 'va' to view all the tasks listed in tasks.txt.
- It displays all tasks in an easy-to-read format, with each task assigned a unique number.

### Viewing User's Assigned Tasks <a name="viewing-users-assigned-tasks"></a>

- The function `view_mine()` is called when users type 'vm' to view all the tasks assigned to them.
- It displays the user's assigned tasks in an easy-to-read format, with corresponding task numbers.
- The user can select a specific task by entering the task number or input '-1' to return to the main menu.

### Editing Tasks <a name="editing-tasks"></a>

- When the user selects 'vm' to view their assigned tasks, they have the option to mark a task as complete or edit the task.
- If the user chooses to mark a task as complete, the 'Yes'/'No' value indicating task completion is changed to 'Yes'.
- If the user chooses to edit a task, they can modify the assigned user or due date, but only if the task has not been completed.

### Generating Reports <a name="generating-reports"></a>

- The main menu of the application includes an option to generate reports.
- When the user chooses to generate reports, two text files are created: task_overview.txt and user_overview.txt.
- task_overview.txt provides a summary of

the tasks tracked in task_manager.py, including the total number of tasks, completed tasks, uncompleted tasks, overdue tasks, percentage of incomplete tasks, and percentage of overdue tasks.
- user_overview.txt provides an overview of the registered users in task_manager.py, including the total number of users, total number of tasks, tasks assigned to each user, percentage of tasks assigned to each user, percentage of completed tasks assigned to each user, percentage of tasks yet to be completed assigned to each user, and percentage of overdue tasks assigned to each user.

### Displaying Statistics <a name="displaying-statistics"></a>

- The menu option to display statistics has been modified to read the reports generated from task_overview.txt and user_overview.txt.
- If the text files don't exist (not generated yet), the code will generate them before displaying the statistics on the screen in a user-friendly manner.


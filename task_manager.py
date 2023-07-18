# Import datetime module
from datetime import date
from datetime import datetime

username_input=input("Please enter your username:\n")
# user to input password 
password_input=input("Please enter your password:\n")
 # Emty list for username
username=[]
 # Empty list for password
password=[]

user_details = {}


# Open user.txt file
# Reads the username and password from user.txt file
with open ('user.txt','r+') as file:
    

    for line in file:
    
     line = line.strip().split(", ") 
     username.append(line[0])  
     password.append(line[1])  

    
# Check if a username or password exists in the file
# If statement ensure that only the admin login to the menu selection
# Else the user will be re-directed to user name and password input
    
while (username_input not in username ) or (password_input not in password):
     
     if (username_input not in username) and (password_input in password):
        print("\nYour username could not be found\n")
        
        
        username_input=input("Please enter your username:\n")
        password_input=input("Please enter your password:\n")
               
        
     elif (username_input in username) and (password_input not in password):
         print("\nYou have entered the wrong password, please re-enter your credentials\n")
         username_input=input("Please enter your username:\n")
         password_input=input("Please enter your password:\n")
             
             
     elif (username_input not in username) and (password_input not in password):
        
        print("Your credentials are incorrect please re-enter\n")
        username_input=input("Please enter your username:\n")
        password_input=input("Please enter your password:\n")
        
     else: 
         print("\nThis login information is correct, please see menu below\n")
               



#Function to register a new user
def reg_user():
    content = ""
    new_user = []
    if username_input  == 'admin':
        new_user_login = False
        new_username = input("\nEnter your username:\n")
        
        while not new_user:
            with open("user.txt", "r+") as afile:
                content = afile.readlines()
                for line in content:
                    new_user = line.split(",")
                    if new_username == new_user[0]:
                        print("Username already exist\n")
                        new_user = True
                        new_username = input("Enter username:\n")
                        
         # Admin user to enter the new password for registration
         # Admin user to enter password for confirmation
        while new_user_login == False:
            new_userpass = input("Enter your password:\n")
            validate_p = input("Confirm your password:\n")
            if new_userpass == validate_p:
                new_user_login = True
            elif new_userpass != validate_p:
                print("Your password do not match, try again.")
                
              # If statement to ensure password and confirm password match
              # New username and password appended to user.txt
            if new_userpass == validate_p:
                print("New user created\n")
                append_user = open('user.txt','a')
                append_user.write("\n" + str(new_username) + ", " + str(validate_p))
                append_user.close()
    else:
        print("Only admin can add new users")
        return menu

# define a function to add tasks
def add_task():

    # Open tasks.txt
    task_file = open('tasks.txt','a')
    # User to input the assigne username
    assignee = input("\nEnter the username you like to assign the work to:\n")
    # User to input the title of the task
    title = input("\nEnter the title of the task:\n")
    # User to input the task description
    description =input("\nDescribe the task:\n")
    # User to input the due date of the task
    due_date = input("\nEnter the task due date dd/mm/yyyy:\n")
    # User to input the current day
    today_date = date.today()
    # Ask user if task has been completed
    completion = "No"  
    if due_date == today_date:
        print("Task is completed.")
    # Write the users answers into tasks.txt
    task_file.write(f"{assignee}, {title}, {description}, {due_date}, {today_date}, {completion}\n")
    task_file.close()


# define view all function
# View all function
# Open/read tasks.txt
# Print out all task present in tasks.txt
def view_all():

    content = ""
    with open('tasks.txt','r') as view_file:
        for line in view_file:
            content = line.split(",")
            
            print(f"""
                      Task : {content[1]}
                      Assigned to : {content[0]}
                      Date assign : {content[3]}
                      Due date : {content[4]}
                      Task Completed : {content[5]}
                      Task description : {content[2]}
                      """)



# View tasks associated with a user
# User has option to edit specific tasks
def view_mine():
    
    task_count= 0

    with open ('tasks.txt','r') as file2:
        for line in file2:

            content = line.strip()
            content = content.split(',')
            task_count += 1

            if content[0] == username_input:

                print(f"""
                    Task {task_count}              : {content[1]}
                    Assigned to         : {content[0]}
                    Date Assigned       : {content[3]}
                    Due Date            : {content[4]}
                    Task complete       :  No
                    Task description    : {content[2]}
                """)
          
         # Ask user to input task number
        task_selection = int(input("Enter the number of the task you want to edit or -1 to go back to the menu: "))

        # If user input is -1 
        # Print menu
        if task_selection == -1:
            return menu
            
        else:
                 # Ask user to select whether they wish to edit or mark as complete
                 selection_option = input("\nWould you like to mark a task as complete or edit a task?\nPlease insert 'mark' or 'edit':\n").lower()
                 
                 # If user selects to mark a task as complete
                 if selection_option == "mark":
                                
                                with open('tasks.txt','r') as file2:
                                 data_line = file2.readlines()
                                 content = data_line[task_selection -1].split(",")
                                 content[5] = "Yes"
                                
                                 data_line[task_selection -1] = str(content)[1:-1].replace('\'', '')
                               
                              # Write the edited line in the tasks file     
                                with open('tasks.txt','w') as file2:
                                 for line in data_line:
                                     file2.writelines(f"{line}\n")
                                 print("\nYour task has been successfully marked as complete\n")
                                
                              
                 elif selection_option == "edit":
                     if content[task_selection][5] == 'No':
                     
                         edit_option = input("\nWould you like to update the task username or due date?\nPlease insert 'name' or 'date':\n").lower()      
                     # If user enter name        
                         if edit_option == 'name':
                                    
                          name_edit = input("\nPlease enter a new username for the task:\n")
                          
                          with open('tasks.txt', 'r') as file:      
                             # read a list of lines into date
                              name_data = file.readlines()
                              content = name_data[task_selection -1].split(",")
                              # Update the line you want to edit
                              name_data[task_selection - 1] = f"{name_edit},{content[1]},{content[2]},{content[3]},{content[4]},{content[5]}"

                         # Write the updated username into the file
                          with open('tasks.txt', 'w') as file:
                            file.writelines(name_data)
                            print("\nYour task has been successfully updated.\n")
                                 
                                 
                        # User selects to edit "date"
                         elif edit_option == 'date':
                       
                          # User to enter a date
                          date_change = input("\nPlease enter a new end date:\nPlease follow the format: YYYY-MM-DD\n")
                                     
                         with open('tasks.txt', 'r') as file:
                                            
                             # read a list of lines into data
                             date_data = file.readlines()
                             content = date_data[task_selection -1].split(",")
                             # Update the line you want to edit
                             date_data[task_selection - 1] = f"{content[0]},{content[1]},{content[2]},{content[3]},{date_change},{content[5]}"
                    
                         # Write the updated username into the file
                         with open('tasks.txt', 'w') as file:
                            file.writelines(date_data)
                            print("\nYour task has been successfully updated.\n")

                 elif selection_option == 'edit':
                     if content[task_selection-1][5] == 'Yes':
                      print(f"Sorry, this task cannot be edited.")



            
# Statistics function
# This function will report the statistics of the tasks
def stats():
    with open('task_overview.txt', 'r') as file:
        for content in file:
            print(content)
    with open('user_overview.txt','r') as afile:
        for line in afile:
            print(line)
            print()
            
# User overview function 
def get_report():
 
    user_list = []
    tasks_list = []
    with open('user.txt','r+') as user_file:
        content = " "
        content = user_file.readlines()
        for line in content:
            strip_cont = line.strip().split(", ")
            # Store users
            user_list.append(strip_cont[0]) 
            
    # Checking the tasks that are assigned per user and calculate they stats
    # Create the useroverview file and write the stats
    # User to enter the username they wish to see statistics for 
    select_user = input("\nSelect a username for statistics:\n")
    if select_user in user_list:
        completed_tasks = 0
        uncompleted_task = 0
        over_due = 0
        total_num_task = 0
    # Open/ read tasks.txt
    with open('tasks.txt','r') as tasks_file:
        lines = tasks_file.readlines()
        for line in lines:
            total_num_task +=1
            strip_cont = line.strip().split(", ")
            # Add all the the tasks titles to tasks list, to find the total number of tasks
            tasks_list.append(strip_cont[1]) 
            if strip_cont[0] == select_user:
                if strip_cont[-1] == 'yes':
                    completed_tasks += 1
                elif strip_cont[-1] == 'no':
                    uncompleted_task += 1
                elif strip_cont[-1]== 'no' and datetime.strftime("%m/%d/%Y") > datetime.today():
                    over_due += 1
                    
    # Calculate the percentages of statistics                   
    total_num_tasks_gen = len(tasks_list)
    per_total_tasks = (total_num_task / len(tasks_list)) * 100
    per_completed_tasks = (completed_tasks / total_num_task) * 100
    per_uncompleted_tasks = (uncompleted_task / total_num_task) *100
    per_over_due_tasks = (over_due/total_num_task) * 100
    # Open/write user_overview.txt
    # Write statistics into the file 
    with open("user_overview.txt",'wt') as file:
        file.writelines(f"The total number of tasks is: {total_num_task}")
        file.writelines(f"\nThe number of completed tasks is : {completed_tasks}")
        file.writelines(f"\nThe number of uncompleted task is: {uncompleted_task}")
        file.writelines(f"\nThe number of overdue_tasks is: {over_due}\n")
        file.writelines(f"\nThe total percentage of the tasks assigned to the user is: {per_total_tasks}")
        file.writelines(f'\nThe percentage of completed tasks is: {per_completed_tasks}')
        file.writelines(f"\nThe percentage of uncompleted tasks is: {per_uncompleted_tasks}")
        file.writelines(f"\nThe percentage of over due tasks: {per_over_due_tasks}")
    print("Reports have been generated")

# Generate reports and create an task_overviewfile
# Initiate all the wanted attribute 
    with open("tasks.txt","rt") as file:
        tasks_list = []
        uncompleted_tasks = 0
        completed_tasks = 0
        over_due_tasks = 0
        total_uncomp_over_due = 0
        content = " "
        content = file.readlines()
        for line in content:
            lines = line.strip().split(", ")
            tasks_list.append(lines[0])
            if lines[-1] == "yes":
                completed_tasks += 1
            elif lines[-1] == "no":
                uncompleted_tasks +=1
            elif lines[-1]== 'no' and datetime.strftime("%m/%d/%Y") > datetime.today():
                over_due_tasks += 1
                
    # Write them on the tasks overview file
    with open('tasks_overview.txt', 'wt') as file:
        total_num_tasks_gen = len(tasks_list)
        total_uncomp_over_due = over_due_tasks + uncompleted_tasks
        per_incomplete = (uncompleted_tasks / total_num_tasks_gen) * 100
        per_over_due_tasks = (over_due_tasks / total_num_tasks_gen) * 100
        file.writelines(f"The total number of generated tasks is: {total_num_tasks_gen}")
        file.writelines(f"\nThe total number of uncompleted tasks is: {uncompleted_tasks}")
        file.writelines(f"\nThe total number of over due tasks is: {over_due_tasks}")
        file.writelines(f"\nThe total number of completed tasks is: {completed_tasks}")
        file.writelines(f"\nThe total number of incomplete and over due tasks tasks is: {total_uncomp_over_due}")
        file.writelines(f"\nThe percentage of incomplete tasks is: {per_incomplete}")
        file.writelines(f"\nThe percentage of overdue tasks is: {per_over_due_tasks}")
                          


while True:

 # If user is admin
 if username_input == "admin":   
              
# Menu for the user once log in
     menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
s - Stats
gr- Generate report
e - Exit
: ''').lower()
     
     
 else:
    
        menu = input('''\nSelect one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()
        


# Calling the functions
 if menu == 'r':
      reg_user()
        
 elif menu == 'a':
      add_task()
      
 elif menu == 'va':
      view_all()
     
 elif menu == 'vm':
      view_mine()
        
 elif menu == 's':
      stats()

 elif menu == 'gr':
      get_report()

 elif menu == 'e':
        print("\nProgram is shutting down.")
        exit()
 else: 
      print("\nYou have not entered an option. Please try again.")
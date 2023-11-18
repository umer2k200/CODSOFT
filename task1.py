import datetime
def take_input():
    while True:
        try:
            print("1. Add a task")
            print("2. View all tasks")
            print("3. Delete a task")
            print("4. Update a task")
            print("5. Exit")
            choice=int(input("Enter the option number: "))
            print("--------------------------------------------------")
            if choice<1 or choice>5:
                print("Invalid input. Please try again.")
                print("--------------------------------------------------")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
            print("--------------------------------------------------")
    return choice
def add_task():
    while True:
        try:
            task=input("Enter the task: ")
            if task=="":
                print("Task cannot be empty. Please try again.")
                print("--------------------------------------------------")
                continue
            while True:
                try:
                    status=input("Enter the status of the task (done/pending): ")
                    if status=="":
                        print("Status cannot be empty. Please try again.")
                        print("--------------------------------------------------")
                        continue
                    if status!="done" and status!="pending":
                        print("Invalid input. Please try again.")
                        print("--------------------------------------------------")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
                    print("--------------------------------------------------")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            print("--------------------------------------------------")
    f1=open("todolist.txt","a")
    f1.close()
    f2=open("todolist.txt","r")
    lines=f2.readlines()
    counter=len(lines)+1
    f2.close()
    f3=open("todolist.txt","a")
    current_dtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f3.write(f"{counter}) [{status}] {task} - ({current_dtime})\n")
    f3.close()
    print("Task added successfully.")
    print("--------------------------------------------------")
def view_task():
    try: 
        f=open("todolist.txt","r")
        lines=f.readlines()
        if len(lines)==0:
            print("No tasks added yet.")
            print("--------------------------------------------------")
        else:
            print("The tasks are:")
            print("--------------------------------------------------")
            for line in lines:
                print(line,end="")
            print("--------------------------------------------------")
        f.close()
    except FileNotFoundError:
        print("File not found. No tasks added yet.")
        print("--------------------------------------------------")
def delete_task():
    try:
        f=open("todolist.txt","r")
        lines= f.readlines()
        f.close()
        if len(lines)==0:
            print("No tasks added yet.")
            print("--------------------------------------------------")
        else:
            view_task()
            while True:
                try:
                    task_no=int(input("Enter the task number to be deleted: "))
                    if task_no<1 or task_no>len(lines):
                        print("Invalid input. Please try again.")
                        print("--------------------------------------------------")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
                    print("--------------------------------------------------")
            f=open("todolist.txt","w")
            counter=1
            for line in lines:
                if line[0]!=str(task_no):
                    f.write(f"{counter})"+line[2:])
                    counter+=1
                else:
                    continue
            f.close()
            print("Task deleted successfully.")
            print("--------------------------------------------------")
    except FileNotFoundError:
        print("File not found. No tasks added yet.")
        print("--------------------------------------------------")
def update_task():
    try:
        f=open("todolist.txt","r")
        lines= f.readlines()
        f.close()
        if len(lines)==0:
            print("No tasks added yet.")
            print("--------------------------------------------------")
        else:
            view_task()
            while True:
                try:
                    task_no=int(input("Enter the task number to be updated: "))
                    if task_no<1 or task_no>len(lines):
                        print("Invalid input. Please try again.")
                        print("--------------------------------------------------")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
                    print("--------------------------------------------------")
            while True:
                try:
                    status=input("Enter the status of the task (done/pending): ")
                    if status=="":
                        print("Status cannot be empty. Please try again.")
                        print("--------------------------------------------------")
                        continue
                    if status!="done" and status!="pending":
                        print("Invalid input. Please try again.")
                        print("--------------------------------------------------")
                        continue
                    break
                except ValueError:
                            print("Invalid input. Please try again.")
                            print("--------------------------------------------------")
            f=open("todolist.txt","w")
            counter=1
            for line in lines:
                if line[0]!=str(task_no):
                    f.write(f"{counter})"+line[2:])
                    counter+=1
                else:
                    if line[4]=="d":
                        task=line[10:]
                    elif line[4]=="p":
                        task=line[13:]
                    f.write(f"{counter}) [{status}] {task}")
                    counter+=1
            f.close()
            print("Task updated successfully.")
            print("--------------------------------------------------")
    except FileNotFoundError:
        print("File not found. No tasks added yet.")
        print("--------------------------------------------------")
def perform_opertions(choice):
    if choice==1:
        add_task()
    elif choice==2:
        view_task()
    elif choice==3:
        delete_task()
    elif choice==4:
        update_task()
def main():
    print("--------------------------------------------------")
    print("      WELCOME TO THE TO-DO LIST APPLICATION       ")
    print("--------------------------------------------------")
    while True:
        choice= take_input()
        if choice==5:
            print("--------------------------------------------------")
            print("Thank you for using the To-Do List Application.")
            print("--------------------------------------------------")
            break
        else:
            perform_opertions(choice)
if __name__ == "__main__":
    main()
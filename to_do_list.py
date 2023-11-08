tasks=[]

def add_task():
    task=input("Enter Your task: ")
    tasks.append(task)
    print("Task added:)\n")
    

def view_task():
    i=1
    print("To-do List")
    for i, task in enumerate(tasks):
        print(i+1, task,"\n")
    

def delete_task():
    num=int(input("Enter a number: "))
    if num <1 or num> len(tasks):
        print("Enter a valid number:\n")
    else:    
        tasks.pop(num-1)
        print("Done\n")

while True:
    print("----------------Choose-----------------")
    print("1:Add task")
    print("2:View task")
    print("3:Delete task")
    print("4:Exit")

    user_choice=int(input("Your choice: "))
    if user_choice==1:
        add_task()
    
    elif user_choice==2:
        view_task()
    
    elif user_choice==3:
        delete_task()
    
    elif user_choice==4:
        break

print("Visit us again:")

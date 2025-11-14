#to-do-list
import json
import os



class ToDoList:
    def  __init__(self,path):
        self.path=path
        self.load_data()
    def load_data(self):
        if not os.path.exists(self.path):
            with open(self.path,"w") as f:
                json.dump([],f)
        with open(self.path,"r")as f:
            self.tasks = json.load(f)
    def save_data(self):
        with open(self.path,"w") as f:
            json.dump(self.tasks,f,indent=4)
            
    def add_tasks(self,tasks):
       self.tasks.append({"task":task,"done":False})
       self.save_data()
    def del_tasks(self,task):
        self.tasks=[t for t in self.tasks if t["task"] != task]
        self.save_data()
    def mark_done(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["done"] = True
                break
        self.save_data()
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n----- YOUR TASKS -----")
        for i, t in enumerate(self.tasks, 1):
            status = "✔ Done" if t["done"] else "✘ Not Done"
            print(f"{i}. {t['task']} - {status}")
        print("-----------------------\n")
print("-----------------TO-DO-LIST------------------")
path = "tasks.json"
todo = ToDoList(path)

while True:
    print("------------ TO-DO MENU ------------")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Done")
    print("4. View Tasks")
    print("5. Exit")
    print("-------------------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task to add: ")
        todo.add_tasks(task)

    elif choice == 2:
        task = input("Enter task to delete: ")
        todo.del_tasks(task)

    elif choice == 3:
        task = input("Enter task to mark as done: ")
        todo.mark_done(task)

    elif choice == 4:
        todo.view_tasks()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
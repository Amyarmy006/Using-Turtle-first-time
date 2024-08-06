print("Welcome to Checklist!")
checklist=[]
def add():
    list=input("Enter Your task")
    checklist.append(list)
    print(checklist)
def del_item():
    list=input("Enter task to be deleted")
    if list in checklist:
        checklist.remove(list)
        print(checklist)
    else:
        print("element not present")
def edit_item():   
    list=input("Enter task to be updated")
    if list in checklist:
        pos=int(input("Enter position"))
        checklist[pos]=list
        print(checklist)
    else:
        print("element not present")
while True:
    option=input("Enter Option(add/update/delete/exit)")
    if option=="add":
        add()
    elif option=="delete":
        del_item()
    elif option=="update":
        edit_item()
    elif option=="exit":
        print("Thank You")
        break
    

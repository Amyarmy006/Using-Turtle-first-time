print("Welcome To contacts")
contact={}
while True:
    print("1.Add contact\n2.Delete contact\n3.update\n4.view contacts\n5.exit")
    option=int(input("Enter option:"))
    if(option==1):
        name=input("Enter name:")
        num=int(input("Enter number"))
        contact[name]=num
        print(contact)
    elif(option==2):
        name=input("Enter name to be deleted:")
        del contact[name]
        print(contact)
    elif(option==3):
        name=input("Enter name of the contact to be updated:")
        num=int(input("Enter Updated number"))
        contact[name]=num
        print(contact)
    elif(option==4):    
        print(contact.keys())
    elif(option==5):
        print("Thank you")
        break
    else:
        print("Enter valid option")

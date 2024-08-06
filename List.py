cart=[]
option=0
while(option<6):
    print("List operation\n1.Add Element\n2.Insert at pos\n3.Remove element\n4.Remove element using index\n5.replace\n6.exit")
    option=int(input("Enter Option"))
    if(option==1):
        element=input("Enter element")
        cart.append(element)
        print(cart)
    elif(option==2):
        pos=int(input("enter position"))
        element=input("Enter element")
        cart.insert(pos,element)
        print(cart)
    elif(option==3):
        element=input("Enter element")
        cart.remove(element)
        print(cart)
    elif(option==4):
        pos=int(input("Enter index"))
        cart.pop(pos)
        print(cart)
    elif(option==5):
        pos=int(input("enter position"))
        element=input("Enter element")
        cart[pos]==element
        print(cart)
    else:    
         print("you Entered Wrong option")

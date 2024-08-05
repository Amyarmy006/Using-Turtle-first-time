import random
number=random.randint(1,10)
print("Welcome to Guess Game!")
i=0
while(i<3):
    guess=int(input("Enter Your Guess:"))
    if(number<guess):
        hint="Your guess is high"
    else:
        hint="Your guess is low"
    if(guess==number):
        print("Your guessed the right answer")
        break
    else:
        print("Sorry!Try Again\n",hint)
    i=i+1
print("The End")

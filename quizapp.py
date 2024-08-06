quiz={'what is Orange cap in ipl:':['low run','highest run','average run','highest run'],'Who won more Ipl tropies':['csk','mi','rcb','csk'],'what is purple cap in IPl':['highest wicket','lowest wicket','no wicket','highest wicket']}
score=0
for q in quiz.keys():
    print(q)
    for v in quiz.values():
        print(v)
        answer=input().lower()
    
    if answer==quiz[q]:
        print("The answer is correct you have scored 1 point!")
        
        score=score+1
    else:
        print("This is an incorrect answer")
print("You have Scored ",score," points")        

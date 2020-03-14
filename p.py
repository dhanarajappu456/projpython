##snake game pyhton
import random  
from PIL import Image
fin=100
pp1=0
pp2=0
turn=0
def show_board():
    print("welcome")
    img=Image.open('LAD.png')
    img.show() 
def check_ladder(pnt):
    if(pnt==1):
        return 38
    elif(pnt==4):
        return 14
    elif(pnt==8):
        return 30
    elif(pnt==8):
        return 30
    elif(pnt==28):
        return 76
    elif(pnt==21):
        return 42
    elif(pnt==50):
        return 67
    elif(pnt==71):
        return 92
    elif(pnt==80):
        return 99
    else: 
        return pnt 
    
def check_snake(pnt):
    if(pnt==36):
        return 6
    elif(pnt==32):
        return 10
    elif(pnt==48):
        return 26
    elif(pnt==8):
        return 30
    elif(pnt==62):
        return 18
    elif(pnt==88):
        return 24
    elif(pnt==95):
        return 56
    elif(pnt==97):
        return 78
    else: 
        return pnt 
        
        
 
 
show_board()

pl1=input("player 1 name")
pl2=input("player 2 name")

print("welcome "+pl1+"&"+pl2)
print("shall we start ??//   press 1 to continue else   0")
l=int(input())

if(l==1):
    while(1):
        if(turn%2==0):
            print(pl1+"please throw the dice")
            c=input("1 to throw 0 to quit ")
        
            if(c=='1'):
                i=random.randint(1,6)
             
                pp1=pp1+i
                if(pp1>fin):
                    print(pl1+" won game")
                    break
                else:    
                    pp1=check_ladder(pp1)
                    pp1=check_snake(pp1)
                    print(pl1,"at",pp1,sep=" ")
            elif(c=='0'):
                    print(p1+" score=",pp1,sep=" ")
                    print(p2+" score=",pp2,sep=" ")
                    break
        else:
            print(pl2+"please throw the dice")
            c=input("1 to throw 0 to quit ")
            if(c=='1'):
                i=random.randint(1,6)
             
                pp2=pp2+i
                if(pp2>fin):
                    print(pl2+" won game")
                    break
                else:    
                    pp2=check_ladder(pp2)
                    pp2=check_snake(pp2)
                    print(pl1,"at",pp2,sep=" ")
            elif(c=='0'):
                print(p1+" score=",pp1,sep=" ")
                print(p2+" score=",pp2,sep=" ")
                break
        turn=turn+1
else:
    printf("quitting",pl1,"score=",pp2,"||||||",pl2,"score=",pp2,sep=" ")     
        
        

        
             
    
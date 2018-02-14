arr=[1,2,3,4,5,6,7,8,9]
import random
arr1=[]
arr2=[]
arrComp=[1,2,3,4,5,6,7,8,9]
t=False
w=False
counter=0
ChoseState=int(input(" 1 player or 2 players :"))
if(ChoseState>2 or ChoseState<1):
    while(ChoseState>2 or ChoseState<1):
        ChoseState=int(input(" 1 player or 2 players :"))
if(ChoseState==2):
    while(counter<9):
        if(t==False and w==False):
            x=int(input("Player 1 :"))
            if(x==0 or x>9):
                while(x==0 or x>9):
                    x=int(input("enter new number player 1 :"))
            if(arr[x-1]=="o"):
                while(arr[x-1]=="o"):
                    if(x==0 or x>9):
                        while(x==0 or x>9):
                            x=int(input("enter new number player 1 :"))
                    x=int(input("enter new number player 1 :"))
                    if(arr[x-1]!="o"):
                        arr1.append(x)
                arr[x-1]="o"
            else:
                arr[x-1]="o"
                arr1.append(x)
            
            for i in arr1:
                if(t==True):
                    break
                for z in arr1:
                    if(t==True):
                        break
                    if(i!=z and i!=x and x!=z and i+z+x==15):
                        print("Player 1 winner ")
                        t=True
                        break
            if(t==False and w == False):
                    y=int(input("Player 2 :"))
                    if(y==0 or y>9):
                        while(y==0 or y>9):
                            y=int(input("enter new number player 2 :"))
                    if(arr[y-1]=="o"):
                        while(arr[y-1]=="o"):
                            y=int(input("enter new number player 2 :"))
                            if(y==0 or y>9):
                                while(y==0 or y>9):
                                    y=int(input("enter new number player 2 :"))
                            if(arr[y-1]!="o"):
                                arr2.append(y)
                        arr[y-1]="o"
                    else:
                        arr[y-1]="o"
                        arr2.append(y)
                         
                    for p in arr2:
                        if(w==True):
                            break
                        for l in arr2:
                             if(w==True):
                                break
                             if(p!=l and l!=y and p!=y and  p+l+y==15):
                                 print("Player 2 winner ")
                                 w=True
                                 break
            counter=counter+1  
    if(w==False and t==False):
        print("Draw")

    
                  
elif(ChoseState==1):
    while(counter<5):
        if(t==False and w==False):
             x=int(input("Player 1 :"))
             if(x==0 or x>9):
                   while(x==0 or x>9):
                      x=int(input("enter new number player 1 :"))
             if((arr[x-1]=="o")or (x==0 or x>9)):
                 while((arr[x-1]=="o")or (x==0 or x>9)):
                     x=int(input("enter new number player 1 :"))
                     if(x==0 or x>9):
                         while(x==0 or x>9):
                             x=int(input("enter new number player 1 :"))
                     if(arr[x-1]!="o"):
                         arr1.append(x)
                 arr[x-1]="o"
                 arrComp.remove(x)
             else:
                 arr[x-1]="o"
                 arrComp.remove(x)
                 arr1.append(x)
            
        for i in arr1:
            if(t==True):
                break
            for z in arr1:
                if(t==True):
                     break
                if(i!=z and i!=x and x!=z and i+z+x==15):
                    print("Player 1 winner ")
                    t=True
                    break
        if(t==False and w== False):
                y=random.choice(arrComp)
                if(arr[y-1]=="o"):
                    while(arr[y-1]=="o"):
                        y=random.choice(arrComp)
                        if(arr[y-1]!="o"):
                            arr2.append(y)
                            print("Player 2 :",y)
                    arr[y-1]="o"
                    arrComp.remove(y)
                else:
                    arr[y-1]="o"
                    arrComp.remove(y)
                    arr2.append(y)
                    print("Player 2 :",y)
                         
                for p in arr2:
                    if(w==True):
                        break
                    for k in arr2:
                            if(w==True):
                               break
                            if(p!=k  and p!=y and k!=y and p+k+y==15):
                                print("Player 2 winner ")
                                w=True
                                break
        counter=counter+1  
    if(w==False and t==False):
        print("Draw")
              

            

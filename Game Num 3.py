arr=[1,2,3,4,5,6,7,8,9]
arr1=[]
arr2=[]
t=False
w=False
counter=0
while(counter<9):
    if(t==False and w==False):
        x=int(input("Player 1 :"))
        if(x==0 or x>9):
            while(x==0 or x>9):
                x=int(input("enter new number player 1 :"))
        if(arr[x-1]=="o"):
            while(arr[x-1]=="o"):
                x=int(input("enter new number player 1 :"))
                if(x==0 or x>9):
                    while(x==0 or x>9):
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
          

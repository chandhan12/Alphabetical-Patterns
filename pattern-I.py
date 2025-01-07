r=5
c=5
for i  in range(r):
    for j in range(c):
        if(i==0 or j==2 or i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")  
    print()
     

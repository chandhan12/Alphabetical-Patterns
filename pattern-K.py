r=5
c=5
for i in range(r):
    for j in range(c):
        if(j==0 or (j==3 and (i==0 or i==4)) or (j==2 and (i==1 or i==3)) or(i==2 and j==1) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()

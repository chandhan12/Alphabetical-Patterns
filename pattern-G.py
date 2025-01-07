r=5
c=5
for i in range(r):
    for j in range(c):
        if((i==0 and j>0) or (j==0 and i>0 and i<4) or (j==4 and i>1) or (i==2 and j>1) or (i==4 and j>0) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
r=5
c=5
for i in range(r):
    for j in range(c):
        if((i==1 and (j==0 or j==4)) or (i==2 and (j==1 or j==3)) or (i==3 and j==2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
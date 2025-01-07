r=5
c=5
for i in range(r):
    for j in range(c):
        if(j==0 or j==4 or (i==1 and (j==1 or j==3)) or (j==2 and i==2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
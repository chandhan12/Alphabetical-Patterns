r=5
c=5
for i in range(r):
    for j in range(c):
        if((i==0 and j<4 or j==0) or(i==1 and j>3) or (i==2 and j<4) ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
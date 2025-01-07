r=5
c=5
for i in range(r):
    for j in range(c):
        if((i==0 and j<3) or j==0 or (i==4 and j<3) ):
            print("*",end=" ")
        elif(j==3 and i>0 and i<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()

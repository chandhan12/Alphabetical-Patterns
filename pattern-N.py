r=5
c=5
for i in range(r):
    for j in range(c):
        if(j==0 or j==4 or i==j ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
r=5
c=5
for i in range(r):
    for j in range(c):
        if(j==0 or i==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
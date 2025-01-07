r=5
c=5
for i in range(r):
    for j in range(c):
        if(i==0 or j==0 or j==4 or i==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
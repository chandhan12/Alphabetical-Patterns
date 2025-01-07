r=6
c=6
for i in range(r):
    for j in range(c):
        if(i==j or j==c-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
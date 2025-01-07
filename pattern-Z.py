r=5
c=5
for i in range(r):
    for j in range(c):
        if(i==0 or i==4 or j==c-1-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
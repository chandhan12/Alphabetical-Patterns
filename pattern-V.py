r=5
c=5
for i in range(r):
    for j in range(c):
        if((i==j and j<3) or  (j==c-1-i and i<3)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
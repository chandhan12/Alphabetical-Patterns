r=5
c=5
for i in range(r):
    for j in range(c):
        if(j==0 or ((i==0 or i==2) and j<3) or(i==1 and j==3) or(i==3 and j==2) or (i==4 and j==3 )):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(end=" ")
    print()
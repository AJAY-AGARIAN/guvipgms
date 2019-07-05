i=int(input())
j=int(input())
for k in range(i+1,j):
    for l in range(2,k):
        if(k%l==0):
            break
        else:
            print(k,end=" ")

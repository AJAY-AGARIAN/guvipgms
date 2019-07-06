h=int(input())
j=int(input())
for i in range(h,j+1):
    for f in range(2,i):
        if(i%f==0):
            break
        else:
            print(i)

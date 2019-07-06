h=int(input())
j=int(input())
count=[]
for i in range(h+1,j+1):
    if(i>1):
        for f in range(2,i):
            if(i%f==0):
                break
        else:
            count.append(f)
print(len(count)+1)

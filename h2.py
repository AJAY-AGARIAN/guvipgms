k=int(input())
i=[]
no=0
for j in range(0,k):
    i.append(input())
p=i
for j in range(0,len(i)):
    for k in range(j+1,len(i)):
        if(i[1:]!=i[:-1]):
            if(p[j]<p[k]):
                temp=p[j]
                p[j]=p[k]
                p[k]=temp
print(''.join(p))

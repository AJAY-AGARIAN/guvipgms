i=int(input())
k=list(map(int,input().split()))
y=[]
count=0
for j in range(0,i):
    if(k[j]==j):
        y.append(j)
        count=count+1
for h in range(0,len(y)):
    for g in range(h+1,len(y)):
        if(y[h]>y[g]):
            temp=y[h]
            y[h]=y[g]
            y[g]=temp
if count<1:
    print('-1')
else:
    print(y)

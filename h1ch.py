import numpy as np
k=int(input())
i=[]
no=0
for j in range(0,k):
    i.append(input())
p=[]
for j in range(0,len(i)):
    for k in range(j+1,len(i)):
        if(i[1:]!=i[:-1]):
            if(i[j]==i[k]):
                p.append(i[j])
                no=no+1
if(no==0):
    print('unique')
elif p:
    unique(p)
def unique(list1): 
    x = np.array(list1) 
    tm=np.unique(x)
    print(''.join(tm))
for c in range(0,len(p)):
    for g in range(c+1,len(p)):
        if(p[c]>p[g]):
            temp=p[g]
            p[g]=p[c]
            p[c]=temp

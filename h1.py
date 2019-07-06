k=int(input())
i=[]
for j in range(0,k):
    i.append(input())
p=[]
for j in range(0,len(i)):
    for k in range(j+1,len(i)):
        if(i[j]==i[k]):
            p.append(i[j])
print(p)
for c in range(0,len(p)):
    for g in range(c+1,len(p)):
        if(p[c]>p[g]):
            temp=p[g]
            p[g]=p[c]
            p[c]=temp
print(''.join(p))

j=list(input())
if(j[0].islower):
    j[0]=j[0].upper()
for k in range(0,len(j)):
    if(j[k]==' '):
        if(j[k+1].islower):
            j[k+1]=j[k+1].upper()
print(''.join(j))

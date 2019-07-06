i=list(input())
for j in range(0,len(i)):
    if(j%2!=0):
        print(i[j])
        temp=i[j-1]
        i[j-1]=i[j]
        i[j]=temp
print(''.join(i))

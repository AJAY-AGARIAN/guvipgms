i=int(input())
j=int(input())
a=[]
for k in range(i+1,j):
    if(k%2==0):
        a.append(k)
        print(k,"",end='')
    

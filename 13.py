i=int(input())
count=0
for j in range(2,i):
    if(i%j==0):
        count=1
        break
    else:
        count=0
if(count>0):
    print('no')
else:
    print('yes')

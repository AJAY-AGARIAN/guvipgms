f=int(input())
f1=int(f)
d=0
while(f>0):
    g=int(f%10)
    f=int((f-g)/10)
    d=(d*10)+g
if(d==f1):
    print('yes')
else:
    print('no')

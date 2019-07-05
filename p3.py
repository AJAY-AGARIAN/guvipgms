s=int(input())
rev=0
while(s>=1):
    d=0
    d=int(s%10)
    s=s/10
    rev=(rev*10)+d
print(rev)
    

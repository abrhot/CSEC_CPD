n=list(map(int,input().split()))
n=sorted(n)
c=0
for i in range(1,4):
    if n[i]==n[i-1]:
        c+=1
print(c)

n,c=list(map(int, input().split()))
k=list(map(int, input().split()))
z=0
for i in k:
    if i > c:
        z+=2
    else:
        z+=1
print(z)



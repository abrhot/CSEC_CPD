n=int(input())
l=[]
count=0
for i in range(n):
    m=input().split()
    l.append(m)
for k in l:
    for o in l:
        if k[0]==o[1]:
            count+=1
print(count)



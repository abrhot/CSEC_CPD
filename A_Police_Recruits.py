n=int(input())
off=0
un=0
crime=list(map(int,input().split()))
for i in crime:
    if i >0:
        off+=i
    else:
        if off >0:
            off-=1
        else:
            un+=1
print(un)



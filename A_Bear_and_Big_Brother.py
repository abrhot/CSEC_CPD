c,k=map(int, input().split())
cnt=0
while True:
    c=c*3
    k=2*k
    cnt+=1
    if c>k:
        break
print(cnt)

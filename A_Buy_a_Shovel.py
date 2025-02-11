b,k=map(int,input().split())
for i in range(1,11):
    if (i*b)%10==0 or (i*b) %10==k:
        print(i)
        break
s
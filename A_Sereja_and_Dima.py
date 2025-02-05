n=int(input())
num=list(map(int,input().split()))
num.sort(reverse=True)
s=0
d=0
for i in range(n):
    if i%2==0:
        s+=num[i]
    else:
          d+=num[i]
print(max(s, d), min(s,d))



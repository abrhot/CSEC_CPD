n=int(input())
p=0
for i in range(n):
    nums=list(map(int, input().split()))
    z=0
    z=nums.count(1)
    if z>=2:
        p+=1
print(p)


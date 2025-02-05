n=int(input())
count=1
m = [input().strip() for k in range(n)] 
for i in range(1,n):
    if m[i]!=m[i-1]:
        count+=1
print(count)
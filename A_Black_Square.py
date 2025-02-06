calori=list(map(int, input().split()))
num=input().strip()
count=0
for n in num:
    count+=calori[int(n)-1]
print(count)

matrx=[]
for i in range(5):
    r=list(map(int, input().split()))
    matrx.append(r)
for i in range(5):
    for j in range(5):
        if matrx[i][j]==1:
            k,l=i,j
print(abs(k-2) + abs(l-2))

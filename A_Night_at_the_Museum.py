word=input().strip()
move=0
posion="a"
for l in word:
    d=abs(ord(l)-ord(posion))
    move+=min(d, 26-d)
    posion=l
print(move)
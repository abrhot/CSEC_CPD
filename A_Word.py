n=input()
capital=0
small=0
for l in n:
    if l.isupper():
        capital+=1
    elif l.islower():
        small+=1
        
if  capital > small:
    print(n.upper())

else:
    print(n.lower())

        

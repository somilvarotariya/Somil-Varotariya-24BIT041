l=[]
def binary(n):
    if n%2==0:
        l.append(0)
    else:
        n=n//2
        l.append(1)
    if  n==0:
        return None
    binary(n//2)
binary(50)
s=len(l)
for i in range(s-1,-1,-1):
    print(l[i],end='')

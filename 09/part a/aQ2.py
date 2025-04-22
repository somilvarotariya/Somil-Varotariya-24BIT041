def compute(n):
    result = n + (n*n) + (n**3) + (n**4)
    return result
l = []
for i in range(4,8):
    l.append(compute(i))
print(l)
    
    

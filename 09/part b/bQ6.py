def sanitize(l1,i=0):
    if i == len(l1):
        return l1
    elif l1[i] < 0:
        l1[i]= 0
    return sanitize(l1,i+1)
l1 = [1,2,3,-4,-5,-6]
print(sanitize(l1))
    
    

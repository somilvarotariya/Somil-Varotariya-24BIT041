def avg(l1,i=1):
    a = l1[i]/(i)
    return avg(l1,i+1)
l1 = [1,2,3,4,5,6]
print(avg(l1))
    

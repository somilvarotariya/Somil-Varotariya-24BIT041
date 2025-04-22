fact = []
def factors(n):
    for i in range(2,n+1):
        if n%i==0:
            fact.append(i)
            factors(n//i)
            break
factors(56)
print(fact)

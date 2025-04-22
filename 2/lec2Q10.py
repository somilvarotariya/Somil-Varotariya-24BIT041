def pr():
    l=int(input("length:"))
    b=int(input("breadth:"))
    p=2*(l+b)
    if l*b>p:
        print("area greater than perimeter")
    else:
        print("not")

pr()

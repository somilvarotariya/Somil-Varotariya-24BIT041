def mark(marks1,marks2,marks3):
    print("total marks is 100")
    x=(marks1+marks2+marks3)/3
    print("average marks is:",x)
    if x>=0 and x<=39 :
        print("F")
    elif x>=40 and x<=44:
        print("P")
    elif x>=45 and x<=49:
        print("C")
    elif x>=50 and x<=54:
        print("B")
    elif x>=55 and x<=59:
        print("B+")
    elif x>=60 and x<=69:
        print("A")
    elif x>=70 and x<=79:
        print("A+")
    elif x>=80 and x<=100:
        print("O")
    else:
        print("NA")

mark(85,92,68)

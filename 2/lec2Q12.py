def circle(x,y,r,x1,y1):
    if ((x-x1)^2+(y-y1)^2)== ((r)^2):
        print("point lies on circle")
    elif ((x-x1)^2+(y-y1)^2)<=((r)^2):
        print("point lies within circle")
    else:
        print("point lies outside circle")

circle(5,5,1,3,3)
    

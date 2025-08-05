x = int(input("X :"))
y = int(input("Y :"))

if x >0 and y>0 :
    print("First Quadrant !")
elif x >0 and y<0 :
    print("fourth Quadrant !")
elif x <0 and y>0:
    print("Second Quadrant !")
elif x<0 and y<0 :
    print("Third Quadrant !")
else :
    if x ==0 :
        print("Y Axis !")
    else :
        print("X Axis !")

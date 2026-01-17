from math import pi

def CircleArea(radius):
    return pi*radius*radius
    
def main():
    No=0
    Ret=0 

    print("Enter the radius : ")
    radius=int(input())
    
    Ret=CircleArea(radius)
    print("Area of circle is ",Ret)
    
if __name__ =="__main__":
    main()
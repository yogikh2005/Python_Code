def RectArea(length,width):
    return length*width
    
def main():
    No=0
    Ret=0 
    print("Enter the length : ")
    length=int(input())
    print("Enter the width : ")
    width=int(input())
    Ret=RectArea(length,width)
    print("Area of rectangle is ",Ret)
    
if __name__ =="__main__":
    main()
def CubeNo(No):
    return No*No*No

def main():
    print("Enter the No : ")
    No=int(input())
    Res=CubeNo(No)
    print("Cube of ",No," is ",Res)
    
if __name__ =="__main__":
    main()	
Square=lambda No : No*No

def main():
    No=0
    Ret=0

    print("Enter the number :")
    No=int(input())

    Ret=Square(No)
    print("Square of number is : " ,Ret)

if __name__=="__main__":
    main()
Cube=lambda No : No**3

def main():
    No=0
    Ret=0

    print("Enter the number :")
    No=int(input())

    Ret=Cube(No)
    print("Cube of number is : " ,Ret)

if __name__=="__main__":
    main()
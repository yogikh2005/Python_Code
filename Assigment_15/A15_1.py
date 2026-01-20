Square=lambda No : No*No

def main():
    No=0
    Ret=list()
    l=list()

    print("Enter the count of number : ")
    Size=int(input())

    print("Enter the number : ")
    for _ in range(Size):
        No=int(input())
        l.append(No)

    Ret=(list(map(Square,l)))
    print("Square of numbers is : " ,Ret)

if __name__=="__main__":
    main()
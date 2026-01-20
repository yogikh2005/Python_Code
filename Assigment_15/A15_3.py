CheckOdd=lambda No : (No%2!=0)

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

    Ret=(list(filter(CheckOdd,l)))
    print("Odd numbers is : " ,Ret)

if __name__=="__main__":
    main()
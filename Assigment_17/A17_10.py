def SumOfDigit(No):
    Sum=0
    while(No>0):
        d=No%10
        Sum+=d
        No//=10
    return Sum

def main():
    No=0
    Ret=0

    print("Enter the no : ")
    No=int(input())

    Ret=SumOfDigit(No)
    print(Ret)

if __name__=="__main__":
    main()
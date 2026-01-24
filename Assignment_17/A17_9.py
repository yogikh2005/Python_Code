def CountDigit(No):
    Cnt=0
    while(No>0):
        No//=10
        Cnt+=1
    return Cnt
def main():
    No=0
    Ret=0

    print("Enter the no : ")
    No=int(input())

    Ret=CountDigit(No)
    print(Ret)

if __name__=="__main__":
    main()
def FrequncyCnt(l,No):
    Cnt=0
    for i in l:
        if i==No:
            Cnt+=1
    return Cnt

def main():
    l=list()
    Size=0
    Res=0
    No=0

    print("Enter the size ")
    Size=int(input())

    print("Enters the numbers")
    for _ in range(Size):
        no=int(input())
        l.append(no)
    
    print("Enter the number to count frequency : ")
    No=int(input())

    Res=FrequncyCnt(l,No)

    print("frequency of number is : ",Res)


if __name__=="__main__":
    main()
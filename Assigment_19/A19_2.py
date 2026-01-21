
Mul=(lambda No1,No2:No1*No2)

def main():
    No1=0
    No2=0
    Res=0

    print("Enter the number : ")
    No1=int(input())
    
    print("Enter the number : ")
    No2=int(input())

    Res=Mul(No1,No2)
    print("Multiplication of number is ",Res)

if __name__=="__main__":
    main()
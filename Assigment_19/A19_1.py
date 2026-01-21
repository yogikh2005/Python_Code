
power=(lambda No:No**2)

def main():
    No=0
    Res=0

    print("Enter the number : ")
    No=int(input())

    Res=power(No)
    print("Power of number is ",Res)

if __name__=="__main__":
    main()
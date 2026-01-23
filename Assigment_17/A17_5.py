def ChkPrime(No):
    flag=False
    for i in range(2,((No//2)+1)):
        if No%i==0:
            flag=True
            break
    return flag

def main():
    No=0
    Ret=False

    print("Enter the no : ")
    No=int(input())
    
    Ret=ChkPrime(No)
    if Ret==False:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__=="__main__":
    main()
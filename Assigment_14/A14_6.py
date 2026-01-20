CheckOdd=lambda No : (No%2!=0)

def main():
    No=0
    Ret=False
    
    print("Enter the number :")
    No=int(input())
    
    Ret=CheckOdd(No)
    print("Number is Odd : " ,Ret)

if __name__=="__main__":
    main()
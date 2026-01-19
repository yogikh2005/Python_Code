CheckOdd=lambda No : True if No%2!=0   else False

def main():
    No=0
    Ret=False
    
    print("Enter the number :")
    No=int(input())
    
    Ret=CheckOdd(No)
    print("Number is Odd : " ,Ret)

if __name__=="__main__":
    main()
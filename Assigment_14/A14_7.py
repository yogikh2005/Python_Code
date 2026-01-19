CheckDivisibleByFive=lambda No : True if No%5==0  else False

def main():
    No=0
    Ret=False
    
    print("Enter the number :")
    No=int(input())
    
    Ret=CheckDivisibleByFive(No)
    print("Number Divisible By 5 is  : " ,Ret)

if __name__=="__main__":
    main()
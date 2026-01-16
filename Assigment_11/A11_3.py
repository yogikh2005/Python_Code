def SumOfDigit(No):
    Sum=0
    while(No>0):
        Sum=Sum+(No%10)
        No=No//10
    return Sum 
    
def main():
    No=0 
    print("Enter the No : ")
    No=int(input())
    Ret=SumOfDigit(No)
    print(Ret)
    
if __name__ =="__main__":
    main()
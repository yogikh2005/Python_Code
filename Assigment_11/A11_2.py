def CountDigit(No):
    No=abs(No)
    Cnt=0
    while(No>0):
        No=No//10
        Cnt=Cnt+1
    return Cnt 
    
def main():
    No=0 
    print("Enter the No : ")
    No=int(input())
    Ret=CountDigit(No)
    print(Ret)
    
if __name__ =="__main__":
    main()
Minimum=lambda No1,No2 : No1 if (No1<No2)  else No2

def main():
    No1=0
    No2=0
    Ret=0
    
    print("Enter the 1st number :")
    No1=int(input())
    
    print("Enter the 2nd number :")
    No2=int(input())

    Ret=Minimum(No1,No2)
    print("Minimum number is : " ,Ret)

if __name__=="__main__":
    main()
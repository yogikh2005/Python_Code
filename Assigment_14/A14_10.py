LargestNo=lambda No1,No2,No3 : No1 if (No1>No2 and No1 >No3) else (No2 if (No2>No3) else No3)

def main():
    No1=0
    No2=0
    No3=0
    Ret=0
    
    print("Enter the 1st number :")
    No1=int(input())
    
    print("Enter the 2nd number :")
    No2=int(input())
    
    print("Enter the 3rd number :")
    No3=int(input())

    Ret=LargestNo(No1,No2,No3)
    print("Largest number is : " ,Ret)

if __name__=="__main__":
    main()
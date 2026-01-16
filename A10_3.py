def Factorial(No):
    Sum=1
    for i in range(1,No+1):
        Sum=Sum*i
    return Sum

def main():
    No=0
    Ret=0
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Factorial(No)
    print(Ret)

if __name__ =="__main__":
    main()	
def factorial(No):
    Res=1
    for i in range(1,No+1):
        Res*=i
    return Res

def main():
    No=0
    Ret=0

    print("Enter the no : ")
    No=int(input())

    Ret=factorial(No)
    print(Ret)
    
if __name__=="__main__":
    main()
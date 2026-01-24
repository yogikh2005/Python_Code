def factorAdd(No):
    Res=0
    for i in range(1,((No//2)+1)):
        if No%i==0:
            Res+=i
    return Res

def main():
    No=0
    Ret=0

    print("Enter the no : ")
    No=int(input())
    
    Ret=factorAdd(No)
    print(Ret)

if __name__=="__main__":
    main()
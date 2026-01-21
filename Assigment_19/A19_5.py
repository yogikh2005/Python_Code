from  functools import reduce

def ChkPrime(No):
    flag=False
    for i in range(2,((No//2)+1)):
        if No%i==0:
            flag=True
            break
    return not flag

def main():
    No=0
    Data=list()

    print("Enter the size : ")
    Size=int(input())
    
    for i in range(Size):
        No=int(input())
        Data.append(No)

    FData=filter(ChkPrime,Data)
    MData=map((lambda No:No*2),FData)

    Res=reduce((lambda No1,No2:No1 if No1>No2 else No2),MData)

    print(Res)


if __name__=="__main__":
    main()
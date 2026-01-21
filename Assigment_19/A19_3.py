from  functools import reduce
def main():
    No=0
    Data=list()

    print("Enter the size : ")
    Size=int(input())
    
    for i in range(Size):
        No=int(input())
        Data.append(No)

    FData=filter((lambda No:(No>=70 and No<=90)),Data)
    MData=map((lambda No:No+10),FData)

    Res=reduce((lambda No1,No2:No1*No2),MData)

    print(Res)


if __name__=="__main__":
    main()
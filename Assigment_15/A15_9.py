def reduceX(Task,Data):
    Res=Data[0]
    for i in range(1,len(Data)):
        Res=Task(Res,Data[i])
    return Res

def main():
    No=0
    Ret=list()
    l=list()

    print("Enter the count of no : ")
    Size=int(input())

    print("Enter the numbers : ")
    for _ in range(Size):
        No=int(input())
        l.append(No)

    Ret=reduceX((lambda No1,No2:No1*No2),l)
    print("Product of elements is : " ,Ret)

if __name__=="__main__":
    main()
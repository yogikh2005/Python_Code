def filterX(Task,Data):
    Ret=list()
    for i in Data:
        Res=Task(i)
        if Res==True:
            Ret.append(i)
    return Ret

def main():
    Str=None
    Ret=list()
    l=list()

    print("Enter the count of string : ")
    Size=int(input())

    print("Enter the string : ")
    for _ in range(Size):
        Str=input()
        l.append(Str)

    Ret=filterX((lambda Str: len(Str)>5),l)
    print("String having size greater than 5 is : " ,Ret)

if __name__=="__main__":
    main()
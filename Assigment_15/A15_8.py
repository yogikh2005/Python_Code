def filterX(Task,Data):
    Ret=list()
    for i in Data:
        Res=Task(i)
        if Res==True:
            Ret.append(i)
    return Ret

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

    Ret=filterX((lambda no:(no%3==0 and no%5==0)),l)
    print("Numbers which divisible by the 3 and 5 is : " ,Ret)

if __name__=="__main__":
    main()
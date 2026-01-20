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

    Ret=filterX((lambda no:(no%2==0)),l)
    print("Even number count is is : " ,len(Ret))

if __name__=="__main__":
    main()
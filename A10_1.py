def Table(No):
    Ret=list()
    for i in range(1,11):
        Res=No*i
        Ret.append(Res)
    return Ret

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Table(No)
 
    for i in Ret:
        print(i,end=" ")    
           
if __name__ =="__main__":
    main()	
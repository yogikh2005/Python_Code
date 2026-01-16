def OddNo(No):
    Ret=list()
    for i in range(1,11):
        if i %2!=0:
            Ret.append(i)
    return Ret

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=OddNo(No)
 
    for i in Ret:
        print(i,end=" ")    
           
if __name__ =="__main__":
    main()	
def Binary(No):
    Res=list()
    while(No>0):
        b=No%2
        Res.append(b)
        No=No//2
    Res.reverse()
    return Res

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Binary(No)
    for i in Ret:
        print(i,end=" ") 
           
if __name__ =="__main__":
    main()	
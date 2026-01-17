def Factors(No):
    Res=list()
    for i in range(1,No+1):
        if No%i==0:
           Res.append(i)
    return Res

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Factors(No)
 
    for i in Ret:
        print(i,end=" ")    
           
if __name__ =="__main__":
    main()	
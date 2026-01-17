def Factors(No):
    Res=0
    for i in range(1,((No//2)+1)):
        if No%i==0:
           Res=Res+i
    return Res

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Factors(No)
    print(Ret)
    if Ret==No:
        print("Perfect Number") 
           
if __name__ =="__main__":
    main()	
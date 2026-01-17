def Dsiplay(No):
    Res=list()
    for i in range(No,0,-1):
           Res.append(i)
    return Res

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Dsiplay(No)
 
    for i in Ret:
        print(i,end=" ")    
           
if __name__ =="__main__":
    main()	
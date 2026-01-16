def CheckPrime(No):
    flag=False
    for i in range(2,(No//2)):
        if No %i==0:
            flag=True
    return flag
            

def main():
    No=0 
    print("Enter the No : ")
    No=int(input())
 
    Ret=CheckPrime(No)
    if Ret==False:
        print("Prime Number")
    

if __name__ =="__main__":
    main()	
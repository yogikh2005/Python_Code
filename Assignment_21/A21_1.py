import threading

def ChkPrime(No):
    flag=False
    for i in range(2,((No//2)+1)):
        if No%i==0:
            flag=True
            break
    return not flag

def DispPrime(Data):
    for i in Data:
        if i==1:
            continue
        if ChkPrime(i)==True:
            print("prime No : ",i)

def DsipNonPrime(Data):
    for i in Data:
        if i==1:
            continue
        if ChkPrime(i)==False:
            print("prime not No : ",i)

def main():
    size=0
    Data=list()

    print("Enter the size  : ")
    size=int(input())

    for i in range(size):
        n=int(input())
        Data.append(n)

    t1=threading.Thread(target=DispPrime,args=(Data,),name="Prime")
    t2=threading.Thread(target=DsipNonPrime,args=(Data,),name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
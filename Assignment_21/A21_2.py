import threading

def MaximumNo(Data):
    print("Max No : ",max(Data))


def MinimumNo(Data):
    print("Min No : ",min(Data))

def main():
    size=0
    Data=list()

    print("Enter the size  : ")
    size=int(input())

    for i in range(size):
        n=int(input())
        Data.append(n)

    t1=threading.Thread(target=MaximumNo,args=(Data,),name="Maximum")
    t2=threading.Thread(target=MinimumNo,args=(Data,),name="Minimum")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
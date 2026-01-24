import threading

def EvenSum(Data):
    Sum=0
    for i in Data:
            if i%2==0:
                Sum+=i
            
    print("Even Sum is : ",Sum)

def OddSum(Data):
    Sum=0
    for i in Data:
            if i%2!=0:
                Sum+=i
    print("Odd Sum is : ",Sum)

def main():
    No=0
    size=0
    Data=list()

    print("Enter the size  : ")
    size=int(input())

    for i in range(size):
        n=int(input())
        Data.append(n)

    OddList=threading.Thread(target=OddSum,args=(Data,))
    EvenList=threading.Thread(target=EvenSum,args=(Data,))

    OddList.start()
    EvenList.start()

    OddList.join()
    EvenList.join()

    print("Exit from main")
if __name__=="__main__":
    main()
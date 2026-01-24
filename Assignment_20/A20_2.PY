import threading

def EvenFactor(No):
    Sum=0
    for i in range(1,No+1):
        if No%i==0:
            if i%2==0:
                Sum+=i
            
    print("Even factors Sum is : ",Sum)

def OddFactor(No):
    Sum=0
    for i in range(1,No+1):
        if No%i==0:
            if i%2!=0:
                Sum+=i
    print("Odd factors Sum is : ",Sum)

def main():
    No=0

    print("Enter the number : ")
    No=int(input())

    t1=threading.Thread(target=OddFactor,args=(No,))
    t2=threading.Thread(target=EvenFactor,args=(No,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
if __name__=="__main__":
    main()
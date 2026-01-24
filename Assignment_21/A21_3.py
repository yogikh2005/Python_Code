import threading

No=0
lobj=threading.Lock()

def Increment(Size):    
    global No

    for _ in range(Size):
        with lobj:
            No+=1

def main():
    size=0

    print("Enter the size  : ")
    size=int(input())

    t1=threading.Thread(target=Increment,args=(size,))
    t2=threading.Thread(target=Increment,args=(size,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Value of No :",No)
    print("Exit from main")

if __name__=="__main__":
    main()
import threading

def EvenDisp():
    No=2
    for _ in range(10):
        print("Even : ",No)
        No+=2

def OddDisp():
     No=1
     for _ in range(10):
        print("Odd : " ,No)
        No+=2    

def main():

    t1=threading.Thread(target=EvenDisp)
    t2=threading.Thread(target=OddDisp)

    t1.start()
    t2.start()


if __name__=="__main__":
    main()
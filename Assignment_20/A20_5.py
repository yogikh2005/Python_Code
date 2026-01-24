import threading

def DispNoAsc():
    for i in range(1, 51):
        print(i)

def DispNoDes():
    for i in range(50, 0, -1):
        print(i)

def main():

    thread1 = threading.Thread(target=DispNoAsc, name="Thread1")
    thread2 = threading.Thread(target=DispNoDes, name="Thread2")

    thread1.start()
    thread1.join() 

    thread2.start()
    thread2.join()

    print("Exit from main")

if __name__=="__main__":
    main()
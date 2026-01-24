import threading

def count_small(str):
    cnt=0
    for i in str:
        if i.islower():
            cnt+=1
    print("Thraed name : ",threading.current_thread().name ,"Thread Id : ",threading.get_ident()," Lower Cnt : ",cnt)


def count_capital(str):
    cnt=0
    for i in str:
        if i.isupper():
            cnt+=1
    print("Thraed name : ",threading.current_thread().name ," Thread Id : ",threading.get_ident()," Upper Cnt : ",cnt)

def count_digits(str):
    cnt=0
    for i in str:
        if i.isdigit():
            cnt+=1
    print("Thraed name : ",threading.current_thread().name ," Thread Id : ",threading.get_ident()," Digit Cnt : ",cnt)

def main():
    str = input("Enter a string : ")

    t1 = threading.Thread(target=count_small, args=(str,), name="Small")
    t2 = threading.Thread(target=count_capital, args=(str,), name="Capital")
    t3 = threading.Thread(target=count_digits, args=(str,), name="Digits")

    
    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
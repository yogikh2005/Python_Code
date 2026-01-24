import threading

def Sum(Data, Result):
    total = 0
    for i in Data:
        total += i
    Result['sum'] = total  

def Mul(Data, Result):
    prod = 1
    for i in Data:
        prod *= i
    Result['mul'] = prod  

def main():
    Data = []
    results = {'sum': 0, 'mul': 0}

    print("Enter the size: ")
    size = int(input())

    print(f"Enter {size} numbers:")
    for i in range(size):
        n = int(input())
        Data.append(n)


    t1 = threading.Thread(target=Sum, args=(Data, results))
    t2 = threading.Thread(target=Mul, args=(Data, results))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
    print("Summation is : ", results['sum'])
    print("Multiplication : ", results['mul'])

    print("Exit from main")

if __name__ == "__main__":
    main()
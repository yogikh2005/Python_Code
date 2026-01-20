from functools import reduce

def main():
    No=0
    Ret=0
    l=list()

    print("Enter the count of number : ")
    Size=int(input())

    print("Enter the number : ")
    for _ in range(Size):
        No=int(input())
        l.append(No)

    Ret=reduce((lambda No1,No2 : No1+No2),l)
    print("Addition of numbers is : " ,Ret)

if __name__=="__main__":
    main()
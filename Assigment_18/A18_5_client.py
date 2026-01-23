from functools import reduce
from MarvellousNum import ChkPrime

def ListPrime(l):
    Res=list()
    for i in l:
        if i==1:
            continue
        if not ChkPrime(i):
            Res.append(i)
    return Res

def AddOfListElemet(l):
    Sum=0
    for i in l:
        Sum+=i
    return Sum

def main():
    l=list()
    Size=0
    Res=list()
    Sum=0

    print("Enter the size ")
    Size=int(input())

    print("Enters the numbers")
    for _ in range(Size):
        no=int(input())
        l.append(no)
    
    Res=ListPrime(l)

    Sum=AddOfListElemet(Res)

    print("Summation of prime number is : ",Sum)


if __name__=="__main__":
    main()
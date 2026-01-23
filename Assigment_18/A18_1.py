from functools import reduce

def main():
    l=list()
    Size=0
    Res=None

    print("Enter the size ")
    Size=int(input())

    print("Enters numbers")
    for _ in range(Size):
        no=int(input())
        l.append(no)
    
    Res=reduce((lambda No1,No2 :No1+No2),l)

    print("Addition of numbers is  : ",Res)


if __name__=="__main__":
    main()
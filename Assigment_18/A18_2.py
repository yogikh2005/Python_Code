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
    
    Res=reduce((lambda No1,No2 :No1 if No1>No2 else No2),l)

    print("Maximum of number is  : ",Res)


if __name__=="__main__":
    main()
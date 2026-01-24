def Add(No1,No2):
        return No1+No2

def main():
    No1=0
    No2=0

    print("Enter the 1st number : ")
    No1=int(input())
    print("Enter the 2nd number : ")
    No2=int(input())

    print(Add(No1,No2))

if __name__=="__main__":
    main()
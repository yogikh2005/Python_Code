def ChkNum(No):
    if No%2==0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    No=0
    print("Enter the number : ")
    No=int(input())
    print(ChkNum(No))

if __name__=="__main__":
    main()
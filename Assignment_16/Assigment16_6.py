def ChkNum(No):

    if No==0:
        return "Zero"

    if No<0:
        return "Negative Number"
    else:
        return "Positive Number"

def main():
    No=0
    print("Enter the number : ")
    No=int(input())
    print(ChkNum(No))

if __name__=="__main__":
    main()
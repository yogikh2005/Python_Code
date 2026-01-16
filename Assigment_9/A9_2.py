def ChkGreater(No1,No2):
    if No1>No2:
        print(No1," is greater")
    else:
        print(No2," is greater")

def main():
    print("Enter the 1st No : ")
    No1=int(input())
    print("Enter the 2nd No : ")
    No2=int(input())
    ChkGreater(No1,No2)
    
if __name__ =="__main__":
    main()
	
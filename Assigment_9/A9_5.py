def CheckDivisibleThreeAndFive(No):
    if No%3==0 and No%5==0:
        return True

def main():
    No=0
    Res=False
    print("Enter the No : ")
    No=int(input())
    Res=CheckDivisibleThreeAndFive(No)
    if Res==True:
        print("Divisible by 3 and 5")

if __name__ =="__main__":
    main()	
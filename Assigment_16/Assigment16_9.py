def DisplayEven(No):
     even=2
     for _ in range(No):
        print(even,end=" ")
        even+=2
    
def main():
    No=0
    print("Enter the number : ")
    No=int(input())
    DisplayEven(No)

if __name__=="__main__":
    main()
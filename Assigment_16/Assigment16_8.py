def Display(No):
     for _ in range(No):
        print("*",end=" ")
    
def main():
    No=0
    print("Enter the number : ")
    No=int(input())
    Display(No)

if __name__=="__main__":
    main()
def Display(No):
    for _ in range(No):
        for j in range(1,No+1):
            print(j,end=" ")
        print()
        
def main():
    No=0

    print("Enter the no : ")
    No=int(input())

    Display(No)

if __name__=="__main__":
    main()
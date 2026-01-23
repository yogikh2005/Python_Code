def Display(No):
    for i in range(No):
        for _ in range(i,No):
            print(" * ",end=" ")
        print()

def main():
    No=0

    print("Enter the no : ")
    No=int(input())

    Display(No)

if __name__=="__main__":
    main()
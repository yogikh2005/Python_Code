def DivibleByFive(No):
    return No%5==0
 

def main():
    No=0
    print("Enter the number : ")
    No=int(input())
    print(DivibleByFive(No))

if __name__=="__main__":
    main()
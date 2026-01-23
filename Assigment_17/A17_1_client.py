from A17_1_module import Add,Sub,Mul,Div

def main():
    No1=0
    No2=0

    print("Enter the 1st number : ")
    No1=int(input())
    
    print("Enter the 2nd number : ")
    No2=int(input())

    print("The Addition of numbers is : ",(Add(No1,No2)))

    print("The Subctration of numbers is : ",(Sub(No1,No2)))
    
    print("The Multiplication of numbers is : ",(Mul(No1,No2)))

    print("The Division of numbers is : ",(Div(No1,No2)))
    
if __name__=="__main__":
    main()
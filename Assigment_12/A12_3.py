def Add(No1,No2):
    return No1+No2

def Sub(No1,No2):
    return No1-No2

def Mul(No1,No2):
    return No1*No2

def Div(No1,No2):
    return No1//No2

def main():
    No=0
   
    print("Enter the 1st No : ")
    No1=int(input())
    print("Enter the 2nd No : ")
    No2=int(input())

    print("The Addition is ",Add(No1,No2))
    print("The Subtraction is ",Sub(No1,No2))
    print("The Multiplication is ",Mul(No1,No2))
    print("The Division is ",Div(No1,No2))
           
if __name__ =="__main__":
    main()	
def ReverseNo(No):
    Rev=0
    Temp=No
    while(No>0):
        d=No%10
        Rev=(Rev*10)+d
        No=No//10
    return (Rev==Temp)
    
def main():
    No=0 
    print("Enter the No : ")
    No=int(input())
    Ret=ReverseNo(No)
    if Ret==True:
        print("Palindrome")

if __name__ =="__main__":
    main()
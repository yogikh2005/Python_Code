class BankAccount:
    ROI=10.5
    
    def __init__(self,A,B):
        self.Name=A
        self.Ammount=B

    def Deposit(self,Amt):
        if Amt >0:
            self.Ammount+=Amt
        else:
            print("Invalid deposit amount")
    
    def Withdraw(self,Amt):
        if self.Ammount > Amt:
            self.Ammount+=Amt
        else:
            print("Insuficint Balenece")
    
    def CalculateInterest(self):
        Interest=(self.Ammount*BankAccount.ROI)//100
        return Interest
             
    def Display(self):
        print(f"{self.Name} your bank balenence :  {self.Ammount} ")

class main:
    
    obj1=BankAccount("Yogiraj",10000)
    obj1.Display()
    obj1.Deposit(20000)
    obj1.Withdraw(15000)
    print("Interest : ",obj1.CalculateInterest())
    
    obj1=BankAccount("Jay",11000)
    obj1.Display()
    obj1.Deposit(21000)
    obj1.Withdraw(7000)
    print("Interest : ",obj1.CalculateInterest())
    
if __name__=="__main__":
    main()
        
class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0
    
    def Accept(self):
        print("Enter the 1st Value : ")
        self.Value1=int(input())
        print("Enter the 2nd Value : ")
        self.Value2=int(input())

    def Addition(self):
        return self.Value1+self.Value2
    
    def Substraction(self):
        return self.Value1-self.Value2
    
    def Multiplication(self):
        return self.Value1*self.Value2
    
    def Division(self):
        return self.Value1//self.Value2
    
def main():
   Ans=0

   obj1=Arithmetic()

   obj1.Accept()
   
   Ans=obj1.Addition()
   print("Addition : ",Ans)

   Ans=obj1.Substraction()
   print("Substraction : ",Ans)
   
   Ans=obj1.Multiplication()
   print("Multiplication : ",Ans)
   
   Ans=obj1.Division()
   print("Division : ",Ans)

   obj2=Arithmetic()

   obj2.Accept()
   
   Ans=obj2.Addition()
   print("Addition : ",Ans)

   Ans=obj2.Substraction()
   print("Substraction : ",Ans)
   
   Ans=obj2.Multiplication()
   print("Multiplication : ",Ans)
   
   Ans=obj2.Division()
   print("Division : ",Ans)
   
if __name__=="__main__":
    main()
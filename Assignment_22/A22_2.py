class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
    
    def Accept(self):
        print("Enter the Radius : ")
        self.Radius=float(input())
    
    def CalculatedArea(self):
        self.Area=self.PI*self.Radius*self.Radius

    def CalculatedCircumference(self):
        self.Circumference=2*self.PI*self.Radius

    def Display(self):
        print("The Radius : ",self.Radius)
        print("The Area : ",self.Area)
        print("The Circumference : ",self.Circumference)

def main():
   obj1=Circle()
   obj1.Accept()
   obj1.CalculatedArea()
   obj1.CalculatedCircumference()
   obj1.Display()

   obj1=Circle()
   obj1.Accept()
   obj1.CalculatedArea()
   obj1.CalculatedCircumference()
   obj1.Display()

if __name__=="__main__":
    main()
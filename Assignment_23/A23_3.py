class Numbers:
    def __init__(self,No):
        self.Value=No
    
    def ChkPrime(self):
        if self.Value<=1:
            return False
        
        for i in range(2,((self.Value)//2)+1):
            if self.Value % i==0:
                return False
            
        return True
    
    def Factors(self):
        Res=list()
        for i in range(1,self.Value):
            if self.Value%i==0:
                Res.append(i)
        return Res

    def SumFactors(self):
        sum=0
        for i in range(1,self.Value):
            if self.Value%i==0:
                sum+=i
        return sum
    
    def ChkPerfect(self):
        return self.SumFactors()==self.Value
    
def main():

    obj1=Numbers(6)
    print(" Prime : ",obj1.ChkPrime())
    print(" Perfect : ",obj1.ChkPerfect())
    print(" Factors : ",obj1.Factors())
    print(" Sum of Factors : ",obj1.SumFactors())

        
    obj1=Numbers(121)
    print(" Prime : ",obj1.ChkPrime())
    print(" Perfect : ",obj1.ChkPerfect())
    print(" Factors : ",obj1.Factors())
    print(" Sum of Factors : ",obj1.SumFactors())

if __name__=="__main__":
    main()
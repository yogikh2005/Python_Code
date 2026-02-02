import os
import sys
import hashlib

def CalculateChechSum(FileName):
        fobj=open(FileName,"rb")
        
        hobj=hashlib.md5()

        Buffer=fobj.read(1000)

        while(len(Buffer)>0):
            hobj.update(Buffer)
            Buffer=fobj.read(1000)
        
        fobj.close()

        return hobj.hexdigest()

def CheckFileSame(FileName1,FileName2):

    if os.path.exists(FileName1)==False:            
            print(FileName1,"no such file exists.")
            return
        
    if os.path.exists(FileName2)==False:            
            print(FileName2,"no such file exists.")
            return
            
    if CalculateChechSum(FileName1)==CalculateChechSum(FileName2):
         return "Success"
    else:
         return "Failure"   
    
def main():
    if (len(sys.argv)==3):
        FileName1=sys.argv[1]
        FileName2=sys.argv[2] 

        Ret=CheckFileSame(FileName1,FileName2)
        print(Ret)

    else:
        print("Invalid arguments are passed")
        print("Valid argument are : python A29_4.py fileName1 fileName2")

if __name__=="__main__":
    main()
import os
import sys

def CopyFile(FileName):
    fobj=open(FileName,"r")
    Data=fobj.read()

    wobj=open("Demo.txt","w")
    wobj.write(Data)

    print("Data copy successfully.")
    fobj.close()
    wobj.close()
    
def main():
    if (len(sys.argv)==2):
        FileName=sys.argv[1]
    
        if os.path.exists(FileName)==False:            
            print(FileName,"no such file exists.")
            return
    
        CopyFile(FileName)
        
    else:
        print("Invalid arguments are passed")
        print("Valid argument are : python A29_3.py fileName")

if __name__=="__main__":
    main()
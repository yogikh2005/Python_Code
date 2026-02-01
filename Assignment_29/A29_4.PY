import os
import sys
import filecmp

def main():
    if (len(sys.argv)==3):
        FileName1=sys.argv[1]
        FileName2=sys.argv[2]

        if os.path.exists(FileName1)==False:            
            print(FileName1,"no such file exists.")
            return
        
        if os.path.exists(FileName2)==False:            
            print(FileName2,"no such file exists.")
            return
            
        if filecmp.cmp(FileName1,FileName2)==True:
            print("Success")
        else:
            print("Failure")

    else:
        print("Invalid arguments are passed")
        print("Valid argument are : python A29_4.py fileName1 fileName2")

if __name__=="__main__":
    main()
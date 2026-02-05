import os

def CountLine(FileName):
    Ret=False
    Cnt=0

    Ret=os.path.exists(FileName)

    if Ret==False:
        print("No such file exists")
        return

    fobj=open(FileName,"r")
    Line=fobj.readlines()

    return len(Line)

def main():
    
    FileName=input("Enter the fle name : ")

    Ret=CountLine(FileName)

    print("Count of lines : ",Ret)

if __name__=="__main__":
    main()
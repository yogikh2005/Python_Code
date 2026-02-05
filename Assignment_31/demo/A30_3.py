import os

def DisplayData(FileName):
    Ret=False

    Ret=os.path.exists(FileName)

    if Ret==False:
        print("No such file exists")
        return

    fobj=open(FileName,"r")
    Line=fobj.readline()

    while len(Line)>0:
        print(Line)
        Line=fobj.readline()

def main():
    
    FileName=input("Enter the fle name : ")

    DisplayData(FileName)

if __name__=="__main__":
    main()
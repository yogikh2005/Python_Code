import os

def CountWords(FileName):
    Ret=False
    Cnt=0

    Ret=os.path.exists(FileName)

    if Ret==False:
        print("No such file exists")
        return

    fobj=open(FileName,"r")
    Line=fobj.readline()

    while len(Line)>0:
        Cnt+=len(list(Line.split(" ")))
        Line=fobj.readline()

    return Cnt

def main():
    
    FileName=input("Enter the fle name : ")

    Ret=CountWords(FileName)

    print("Words Count is : ",Ret)

if __name__=="__main__":
    main()
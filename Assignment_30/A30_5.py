import os

def CheckWord(FileName,Word):
    Ret=False

    Word=Word.lower()

    Ret=os.path.exists(FileName)

    if Ret==False:
        print("No such file exists")
        return

    fobj=open(FileName,"r")
    Line=fobj.readline()

    while len(Line)>0:
        if Word in list(Line.lower().split(" ")):
            return True
        Line=fobj.readline()

    return False
def main():
    
    FileName=input("Enter the fle name : ")
    Word=input("Enter the word : ")

    Ret=CheckWord(FileName,Word)

    if Ret==True:
        print(f"{Word} is found in {FileName}")
    else:
        print(f"{Word} is not found in {FileName}")

if __name__=="__main__":
    main()
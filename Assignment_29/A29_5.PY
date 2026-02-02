import os

def CountString(FileName,string):
    cnt=0

    Ret=False
    Ret=os.path.exists(FileName)

    if(Ret==False):
         print("There no such file")
         return
    
    fobj=open(FileName,"r")

    Buffer=fobj.read(1014)
    
    while len(Buffer)>0:
        cnt += Buffer.lower().count(string.lower())
        Buffer=fobj.read(1014)
            
    fobj.close()
    return cnt

def main():
    FileName=input("Enter the file name : ")
    string=input("Enter string to serach : ")
    
    Ret=CountString(FileName,string)
    print(f"Frequency of {string} in {FileName} is {Ret}")
    

if __name__=="__main__":
    main()
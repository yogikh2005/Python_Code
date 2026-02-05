import os

def CopyFile(FileName,NewFile):  
    Ret=False
    
    Ret=os.path.exists(FileName)

    if Ret==False:    
        print(FileName,"no such file exists.")
        return
          
    fobj=open(FileName,"r")
    wobj=open(NewFile,"w")
    
    Buffer=fobj.read(1024)

    while len(Buffer)>0:
        wobj.write(Buffer)
        Buffer=fobj.read(1024)

    print("Data copy successfully.")
    fobj.close()
    wobj.close()
    
def main():

    FileName=input("Enter file name from which data copy : ")
    NewFile=input("Enter NewFile name : ")    

    CopyFile(FileName,NewFile)
    
if __name__=="__main__":
    main()
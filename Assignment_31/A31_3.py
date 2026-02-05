import sys
import os
import time

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

    fobj.close()
    wobj.close()
    
def DirectoryFileCopy(DirectoryName,NewDirectory):
    Ret=False
    timeStamp=time.ctime()

    Ret=os.path.exists(DirectoryName)
    if Ret==False:
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirectoryName)
    if Ret==False:
        print("It's no directory")
        return
    
    Ret=os.path.exists(NewDirectory)
    if Ret==False:
        os.mkdir(NewDirectory)
    
    LogFolder="LogFiles"
    Ret=os.path.exists(LogFolder)

    if Ret==False:
        os.mkdir(LogFolder)
    
    FileName="YK %s.log" %(timeStamp)
    FileName=FileName.replace(":","_")
    FileName=FileName.replace(" ","_")
    FileName=os.path.join(LogFolder,FileName)

    fobj=open(FileName,"w")
    Border="*"*40

    fobj.write(Border+"\n")
    fobj.write("This is log file created by YK Automation\n")
    fobj.write("This is Directory File Copy Script\n")
    fobj.write(Border+"\n")
    fobj.write("File are :\n")

    cnt=0

    for FolderName,_,FileName in os.walk(DirectoryName):

        for Fname in FileName:
            fname=os.path.join(FolderName,Fname)
            NewFile=os.path.join(NewDirectory,Fname)
            CopyFile(fname,NewFile)
            fobj.write(fname+"\n")
            cnt+=1
                
    fobj.write(Border+"\n")
    fobj.write("Total File Copyed : "+str(cnt)+"\n")
    fobj.write("This log file is created at : "+timeStamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("-----Thank You Using YK Automation-----"+"\n")
    fobj.write(Border+"\n")
    fobj.close()

def main():
    if (len(sys.argv)!=3):
        print("Invalid arguments passed")
        print("Valid arurments is : python A31_1.py DirectoryName NewDirectoryName")
        return
    
    DirectoryName=sys.argv[1]
    NewDirectory=sys.argv[2]

    DirectoryFileCopy(DirectoryName,NewDirectory)

if __name__=="__main__":
    main()
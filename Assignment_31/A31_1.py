import sys
import os
import time

def SerachExtension(DirectoryName,Extension):
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
    fobj.write("This is Extension found Script\n")
    fobj.write(Border+"\n")
    fobj.write("File are :\n")

    cnt=0

    for FolderName,_,FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            _,fileExtension=os.path.splitext(fname)
            if fileExtension==Extension:
                fobj.write(fname+"\n")
                cnt+=1
                
    fobj.write(Border+"\n")
    fobj.write("Total File Found : "+str(cnt)+"\n")
    fobj.write("This log file is created at : "+timeStamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("----Thank You Using YK Automation----"+"\n")
    fobj.write(Border+"\n")
    fobj.close()

def main():
    if (len(sys.argv)!=3):
        print("Invalid arguments passed")
        print("Valid arurments is : python A31_1.py DirectoryName Extension")
        return
    
    DirectoryName=sys.argv[1]
    Extension=sys.argv[2]

    SerachExtension(DirectoryName,Extension)

if __name__=="__main__":
    main()
import sys
import os
import hashlib
import time

def CalculateCheckSum(File):
    mobj=hashlib.md5()

    fobj=open(File,"rb")
    Buffer=fobj.read(1024)

    while len(Buffer) >0:
        mobj.update(Buffer)
        Buffer=fobj.read(1024)
        
    fobj.close()
    return mobj.hexdigest()

def FindDuplicate(DirectorytName="Demo"):

    Dict={}

    for FolderName,_,FileName in os.walk(DirectorytName):

        for fname in FileName:
            fname=os.path.join(FolderName,fname)
            checksum=CalculateCheckSum(fname)

            if checksum in Dict:
                Dict[checksum].append(fname)
            else:
                Dict[checksum]=[fname]
    return Dict
            
def DisplayDubplicate(DirectortName="Demo"):
    Ret=False
    timeStamp=time.ctime()

    Ret=os.path.exists(DirectortName)
    if Ret==False:
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirectortName)
    if Ret==False:
        print("It's not directory")
        return
    
    Res=FindDuplicate(DirectortName)

    FData=list(filter(lambda x:len(x)>1,Res.values()))

    LogFilePath="LogFiles"
    Ret=os.path.exists(LogFilePath)

    if Ret==False:
         os.mkdir(LogFilePath)
        
    LogFileName="Log %s.txt" %(time.ctime())
    LogFileName=LogFileName.replace(":","_")
    LogFileName=LogFileName.replace(" ","_")

    LogFileName=os.path.join(LogFilePath,LogFileName)

    Border="-"*40

    fobj=open(LogFileName,"w")
    fobj.write(Border+"\n")
    fobj.write("This log file was created by YK Automation.\n")
    fobj.write("This is a Duplicate File Finder script.\n")
    fobj.write(Border+"\n")

    fobj.write("File Are : \n")

    cnt=0

    for Files in FData:
        for File in Files:
            cnt+=1
            fobj.write(File+"\n")
            
    fobj.write(Border+"\n")
    fobj.write("Total duplicate files found: " + str(cnt) + "\n")
    fobj.write("This log file was created on: " + timeStamp + "\n")
    fobj.write(Border+"\n")
    fobj.write("-----Thank you for using YK Automation----\n")
    fobj.write(Border+"\n")
    fobj.close()
            
def main():
    if len(sys.argv)!=2:
        print("Invalid Arguments passed")
        print("Valid Argumests Are : python A32_2.py DirctoryName")
        return
    
    DirectoryName=sys.argv[1]
    DisplayDubplicate(DirectoryName) 

if __name__=="__main__":
    main()
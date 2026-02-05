import sys
import os
import hashlib

def CalculateCheckSum(File):
    mobj=hashlib.md5()

    fobj=open(File,"rb")
    Buffer=fobj.read(1024)

    while len(Buffer) >0:
        mobj.update(Buffer)
        Buffer=fobj.read(1024)
        
    fobj.close()
    return mobj.hexdigest()

def DisplayCheckSum(DirectortName):
    Ret=False

    Ret=os.path.exists(DirectortName)
    if Ret==False:
        print("There is no such directory")
        return
    
    Ret=os.path.isdir(DirectortName)
    if Ret==False:
        print("It's not directory")
        return
    
    for Folder,_,File in os.walk(DirectortName):

        for fname in File:
            fname=os.path.join(Folder,fname)
            print(f"{fname}:{CalculateCheckSum(fname)}")
    
def main():
    if len(sys.argv)!=2:
        print("Invalid Arguments passed")
        print("Valid Argumests Are : python A32_1.py DirctoryName")
        return
    
    DirectoryName=sys.argv[1]
    DisplayCheckSum(DirectoryName) 

if __name__=="__main__":
    main()
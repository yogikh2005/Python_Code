import os

def main():
    FileName=input("Enter the file name : ")
    
    if os.path.exists(FileName):
           
        fobj=open(FileName,"r")
        Data=fobj.read()

        print("Data from the file : ",Data)
        fobj.close()
    else:
        print(FileName,"no such file exists.")

if __name__=="__main__":
    main()
import os

def main():
    FileName=input("Enter the file name : ")
    string=input("Enter string to serach : ")
    cnt=0

    if os.path.exists(FileName):

        fobj=open(FileName,"r")
        for line in fobj:
            cnt += line.lower().count(string.lower())

        fobj.close()
        print(f"Frequency of {string} in {FileName} is {cnt}")
    else:
        print(FileName,"no such file exists.")

if __name__=="__main__":
    main()
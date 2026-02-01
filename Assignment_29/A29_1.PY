import os

def main():
    FileName=input("Enter the file name")
    
    if os.path.exists(FileName):
            print(FileName," is exits.")
    else:
         print(FileName,"no such file exists.")

if __name__=="__main__":
    main()
def LenX(Str):
    cnt=0
    for i in Str:
        cnt+=1
    return cnt
    
def main():
    No=0
    print("Enter the Name : ")
    Name=input()
    print(LenX(Name))

if __name__=="__main__":
    main()
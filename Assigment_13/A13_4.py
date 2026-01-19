def Binary(No):# 7
    Res=list()
    while(No>0): # 7 3 1 0
        b=No%2 # 1 1 1
        Res.append(b) # 1 1 1
        No=No//2 # 3 1 0
    Res.reverse() # 111
    return Res #111

def main():
    No=0
    Ret=list()
 
    print("Enter the No : ")
    No=int(input())
 
    Ret=Binary(No)
    for i in Ret:
        print(i,end=" ") 
           
if __name__ =="__main__":
    main()	
def Grade(Mark):
    Res=None
    if Mark>=75:
        Res="Distination"
    elif Mark>=60 and Mark<75:
        Res="First class"
    elif Mark>=50 and Mark<60:
        Res="Second class"
    else:
        Res="Fail"       
    return Res

def main():
    No=0

    print("Enter the Mark : ")
    No=int(input())
 
    Ret=Grade(No)
    print("Your grade is ",Ret)
           
if __name__ =="__main__":
    main()	
class BooKStore:
    NoOfBooks=0
    
    def __init__(self,A,B):
        self.Name=A
        self.Author=B
        BooKStore.NoOfBooks+=1

    def Display(self):
        print(f"{self.Name} by {self.Author} . No of books : {BooKStore.NoOfBooks}")

class main:
    obj1=BooKStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj2=BooKStore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__=="__main__":
    main()
        
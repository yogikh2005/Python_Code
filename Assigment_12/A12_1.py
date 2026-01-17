def CheckVowel(Ch):
    Ch=Ch.lower()
    vowel=['a','i','e','o','u']
    if Ch in vowel:
        return "Vowel"
    else:
        return "Consonant"
def main():
    print("Enter the Character : ")
    Ch=input()
    Ret=CheckVowel(Ch)
    print(Ret)
 
if __name__ =="__main__":
    main()
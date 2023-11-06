ch=input("enter the character: ")
if((ch>="a") and (ch<="z") or (ch>="A") and (ch<="z")):
    print("alphabets")
else:
    print("invalid")

##check if vowels or consonants

ch=input("enter the character: ")
if((ch=="a") or (ch=="e") or (ch=="i") or (ch=="o") or (ch=="u")):
    print("its vowels")
elif((ch>="a") and (ch<="z")):
    print("its consonants")
else:
    print("invalid")

 
##check if vowels or consonants or digits

ch=input("enter any character: ")
if((ch>="a") and (ch<="z") or (ch>="A") and (ch<="z")):
    print("alphabets")
elif((ch>="0") and (ch<="9")):
    print("its digits")
else:
    print("special characters")     

    

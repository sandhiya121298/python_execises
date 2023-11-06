##reverse order
for i in range(10,-5,-1):
    print(i)

##end means print same line
print("hello ", end="")
print("python")

##print 1 to 10 numbers using end(new line)
for i in range(1,11):
    print(i,end="|")
    if(i%5==0):
     print()
##print stars using user input
a=int(input("enter the value a: "))
for a in range(a+1):
    for a in range(a):
        print("*" ,end="")
    print()

b=int(input("enter the value b: "))
for i in range(b+1):
    for i in range(b):
        print("*" ,end="")
    print()

word=input("enter the names: ")
x=""
for i in word:
    x+=i
    print(x)

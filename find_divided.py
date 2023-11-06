##check even or add number and divisable by same table

a=int(input("enter the value: "))
b=int(input("enter the value: "))
if((a%5==0)and (a%11==0)):
    print("divisable by 5 and 11")
elif(a%5==0):
    print("divisable by 5")
elif(a%11==0):
    print("divisable by 11")
if(a%2==0):
     print("even number")
else:
     print("odd number")


##check wheather leap year or not

yr=int(input("enter the year: "))

if((yr%4==0) and (yr%100!=0)):
   print("leap year")
else:
   print("commen year")
     

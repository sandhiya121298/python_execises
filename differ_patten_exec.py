for i in range(65,70):
    for j in range(65,70):
        print(chr(j),end=" ")
    print()


for i in range(65,90):
    if(i%5==0):
        print()
    print(chr(i),end=" ")
print()
print()


for i in range(1,26):
    print ("{:2d}".format(i) ,end=" ")
    if(i%5==0):
        print()
print()        


rows=5
cols=5
for i in range(1,rows+1):
    for j in range(i, i+cols*rows, rows):
        print ("{:2d}".format(j) ,end=" ")
    print()
print()    

for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end="")
    print()
print()    


for a in range(65,70):
    for i in range(65,70):
        print(chr(a) ,end="")
    print()
print()     

for i in range(1,50,2):
    print ("{:2d}".format(i) ,end=" ")
    if(i%5==0):
        print()
print()
print() 

for i in range(2,51,2):
    print ("{:2d}".format(i) ,end=" ")
    if(i%5==0):
        print()
print()        

for i in range(5):
    for j in range(5):
        if(j%2==0):
            print(0, end="")
        else:
            print(1,end="")
    print()
print()    


for i in range(5):
    for j in range(5):
        print(abs(i-j),end="")
    print()
print()    
    
for i in range(1,6):
    for j in range(1,6):
        print("{:3d}".format((2*(i+j))-3),end="")
    print()    
    

    

    
      
            
    
    

    
    

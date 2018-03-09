n=int(input("enter"))
q=int(input("enter"))
print(str(n)+" "+str(q))
for i in range(n+1,q):
    if(i%2==0):
        print(i,end=" ")
    

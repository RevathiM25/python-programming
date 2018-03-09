n=int(input("enter"))
for i in range(2,n):
    n%i==0
    break
if(n%n==0 or n%i==0):
    print("yes")
else:
    print("no")
    

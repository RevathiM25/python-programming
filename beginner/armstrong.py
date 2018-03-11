n=int(input("enter"))
temp=n
i=0
while(temp>0):
    dig=temp%10
    i+=dig**3
    temp//=10
if(n==i):
    print("yes")
else:
    print("no")
    

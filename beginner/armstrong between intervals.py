lower=int(input("enter"))
upper=int(input("enter"))
for n in range(lower,upper+1):
    temp=n
    i=0
    while(temp>0):
        dig=temp%10
        i+=dig**3
        temp//=10
    if(n==i):
        print(i)

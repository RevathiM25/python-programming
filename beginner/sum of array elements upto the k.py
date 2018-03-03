lst=[]
s=0
n=int(input("enter"))
l=int(input("enter"))
for i in range(n):
    lst.append(int(input()))
print(lst)
for i in range(k):
    s=s+lst[i]
print(s)

n=int(input("Enter the number:"))
a=n
s=0
for i in range(1,n): 
    if (n%i)==0:
        s=s+i
if s==a:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")

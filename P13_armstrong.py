n=int(input("Enter the number:"))
a=n
d=0
b=0
while n>0:
    d=n%10
    b = b + d*d*d
    n=n//10
if b==a:
    print("armstrong")
else:
    print("Not armstrong")

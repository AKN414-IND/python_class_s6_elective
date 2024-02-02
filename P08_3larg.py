a=int(input("Enter first :"))
b=int(input("Enter second :"))
c=int(input("Enter third :"))

if a>=b and a>=c:
    print(a)
elif b>=c and b>=a:
    print(b)
elif c>=b and c>=a:
    print(c)
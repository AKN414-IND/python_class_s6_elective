def fact(m):
    f=1
    for i in range(1,m+1):
        f=f*i
    return f
n=int(input("n:"))
r=int(input("r:"))
s=fact(n)/(fact(r)*fact(n-r))
print(s)
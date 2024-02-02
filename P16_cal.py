import math
def add(m,n):
    print(m+n)
def sub(m,n):
    print(m-n)
def mul(m,n):
    print(m*n)
def div(m,n):
    print(m/n)
def power(m,n):
    print(math.pow(m,n))
    
a=int(input("Enter the first no:"))
b=int(input("Enter the second no:"))
print("1:add 2:sub 3:mul 4:div 5:pow")
c=int(input("choice:"))
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    mul(a,b)
elif c==4:
    div(a,b)
elif c==5:
    power(a,b)
else:
    print("Invalid Choice!")


n=int(input("enter the limit to check:"))   
largest=0
for i in range (0,n):
    a=int(input("Enter the number:"))
    if(a>largest):
        largest=a
print("The largest number is:",largest)

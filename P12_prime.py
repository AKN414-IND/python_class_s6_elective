def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    print("prime")

n=int(input("value"))
prime(n)
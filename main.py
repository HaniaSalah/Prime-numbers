n1=int(input("n1 ="))

for n in range(2,n1+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n,"is a prime number")
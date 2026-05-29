n=int(input("Enter a number:"))
c=0
a=1
z=0
z=n
while(a<=n):
    if(n%a==0):
        c=c+1
    a=a+1
if(c==2):
    n=z
    f=0
    g=1
    fc=0
    dc=0
    while(n>0):
        x=n%10
        dc=dc+1
        n=n//10
        f=0
        g=1
        while(g<=x):
            if(x%g==0):
                f=f+1
            g=g+1
        if(f==2):
            fc=fc+1
    if(dc==fc):
        print(z,"is a Prime number with Prime digits")
    else:
        print(z,"is a Prime number without Prime digits")
else:
    print(z," is not a prime number")
            



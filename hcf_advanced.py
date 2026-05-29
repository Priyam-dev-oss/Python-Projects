def hcf(a,b):
    c=min(a,b)
    for i in range(1,c+1):
        if(a%i==0 and b%i==0):
            h=i
    return h
k=int(input("How many numbers do you want?"))
r=int(input("Enter number 1:"))
for g in range(2,k+1):
    v=int(input(f"Enter number {g}:"))
    r=hcf(r,v)
print("HCF is :",r)

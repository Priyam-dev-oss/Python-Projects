n=int(input("Enter the first number:"))
a=int(input("Enter the second number:"))
c=min(n,a)
for i in range(1,c+1):
   if(n%i==0 and a%i==0):
      hcf=i
print("The H.C.F of",n,"and",a,"is:",hcf)
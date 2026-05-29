n=int(input("Enter the number:"))
v=n
s=0
while(n>0):
    x=n%10
    s=s*10+x
    n=n//10
if(v==s):
    print(v,"is a apalindrome")
else:
    print(v,"is not a apalindrome")

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
op=input("Enter what you want to do?")
def calculator(a,b,op):
    if(op=="+"):
        return(a+b)
    elif(op=="-"):
        return(a-b)
    elif(op=="*"):
        return(a*b)
    elif(op=="/"):
        return(a/b)
    else:
        print("Something went wrong!")
print(calculator(a,b,op))

    
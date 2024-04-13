def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def Divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
#create a dict where keys are symbols
#and values are name of the functions
operations = {'+':add,'-':subtract,"/":Divide,'*':multiply}

num1 = int(input("What is the first number?:"))
num2 = int(input("What is the Second number?:"))
#loopin thru the dict 


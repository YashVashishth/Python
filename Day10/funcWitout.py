#have to take two parameters 

def withoutPut(firstN,lastN):
    first = firstN.title()
    last = lastN.title()
    return first + last #this replace everything where function was called
# or just return firstN.title() + lastN.title()

firstN = input("Enter the first name :\n")
lastN = input("Enter the last name:\n")
Tname = withoutPut(firstN,lastN)    
print(Tname)
'''Q1. Find the solution of x^3-x-1 = 0 by using the bisection
       method correct to four decimal point.'''

import math 

# *** Bisection method for normal Value ***

# find roots value
def findRootValue(x):
    lowerRoot = x-1
    greaterRoot = x
    storeVal = []
    x1 = 0
    check = 0
    
    while(len(storeVal) < 2 or storeVal[-1] != storeVal[-2]):
        x1 = round((lowerRoot+greaterRoot)/2,4)
        print(f"x{(len(storeVal)+1)} = ({lowerRoot} + {greaterRoot}) / 2 = {x1}\n")
        check = findRoot(x1)
        if(check < 0):
            lowerRoot = x1
        elif(check > 0):
            greaterRoot = x1
        storeVal.append(x1)
    print(f"Your answer getting into x{len(storeVal)} iteration")
    print(f"x approximate | {storeVal[-1]}")

def findRoot(i): # this is the findRoot function which provide root using
                 # equtions.
    val = round(((i**3)-(10*i)-1),7)
    if(val > 0):
        print(f"f({i}) = x**{i} + {i} - 11 = {val} ... {val} > 0\n")
    elif(val < 0):
        print(f"f({i}) = x**{i} + {i} - 11 = {val} ... {val} < 0\n")
    return val


'''print("\nLet, f(x) = x^3-x-1 \n")
j = 0   # Declare variable and empty list
val = []; # This is the list where all root are store
i = 0
while(not val or True): # The loop continues until a greater root is not found.
    val.append(findRoot(j))
    if(val[-1] < 0):
        i += 1
    elif(i > 0 and val[-1] > 0):
        break
    j+=1
    
print("\nso, Root lies between ",j-1," and ",j,"\n")

findRootValue(j)'''

# *** Bisection method for Trigonometric Value ***

'''2). Solve the eqution x - cosx = 0 by using bisection
       method up to 3 decimal point.'''

def findTrigoRootValue(x):
    lowerRoot = x-1
    greaterRoot = x
    storeVal = []
    x1 = 0
    check = 0
    
    while(len(storeVal) < 2 or storeVal[-1] != storeVal[-2]):
        x1 = round((lowerRoot+greaterRoot)/2,3)
        print(f"x{(len(storeVal)+1)} = ({lowerRoot} + {greaterRoot}) / 2 = {x1}\n")
        check = findTrigoRoot(x1)
        if(check < 0):
            lowerRoot = x1
        elif(check > 0):
            greaterRoot = x1
        storeVal.append(x1)
    print(f"Your answer getting into x{len(storeVal)} iteration")
    print(f"x approximate | {storeVal[-1]}")

def findTrigoRoot(i): # this is the findRoot function which provide root using
                 # equtions.
    val = round((math.sin(i))-i**3-1,7)
    if(val > 0):
        print(f"f({i}) = {i} * sin({i}) + cos({i}) = {val} ... {val} > 0\n")
    elif(val < 0):
        print(f"f({i}) = {i} * sin({i}) + cos({i}) = {val} ... {val} < 0\n")
    return val

    

print("\nLet, f(x) = x*sinx*cosx \n")
j = 0   # Declare variable and empty list
val = [] # This is the list where all root are store
i = 0
while(not val or True): # The loop continues until a greater root is not found.
    val.append(findTrigoRoot(j))
    if(val[-1] < 0):
        i += 1
    elif(i > 0 and val[-1] > 0):
        break
    j+=1
    
print("\nso, Root lies between ",j-1," and ",j,"\n")
findTrigoRootValue(j)

# *** Bisection method for Logarithm value ***
'''3). Solve the equation x.log10^x-1.2 = 0 using bisection
       method three decimal places.'''

def findLogRootValue(x):
    lowerRoot = x-1
    greaterRoot = x
    storeVal = []
    x1 = 0
    check = 0
    
    while(len(storeVal) < 2 or storeVal[-1] != storeVal[-2]):
        x1 = round((lowerRoot+greaterRoot)/2,3)
        print(f"x{(len(storeVal)+1)} = ({lowerRoot} + {greaterRoot}) / 2 = {x1}\n")
        check = findLogRoot(x1)
        if(check < 0):
            lowerRoot = x1
        elif(check > 0):
            greaterRoot = x1
        storeVal.append(x1)
    print(f"Your answer getting into x{len(storeVal)} iteration")
    print(f"x approximate | {storeVal[-1]}")

def findLogRoot(i): # this is the findRoot function which provide root using
                 # equtions.
    val = round(((i*math.log10(i))-i-1.2),7)
    if(val > 0):
        print(f"f({i}) = {i} * log10({i}) - 1.2 = {val} ... {val} > 0\n")
    elif(val < 0):
        print(f"f({i}) = {i} * log10({i}) - 1.2 = {val} ... {val} < 0\n")
    return val


'''print("\nLet, f(x) = x*log10^x-1.2 \n")
j = 1   # Declare variable and empty list
val = []; # This is the list where all root are store
i = 0
while(not val or True): # The loop continues until a greater root is not found.
    val.append(findLogRoot(j))
    if(val[-1] < 0):
        i += 1
    elif(i > 0 and val[-1] > 0):
        break
    j+=1
    
print("\nso, Root lies between ",j-1," and ",j,"\n")

findLogRootValue(j)'''

# *** Bisection method for Algebric value ***
'''3). Solve the eqution x*e^x-3 = 0 using the bisection method
from three decimal places.'''

def findAlgeRootValue(x):
    lowerRoot = x-1
    greaterRoot = x
    storeVal = []
    x1 = 0
    check = 0
    
    while(len(storeVal) < 2 or storeVal[-1] != storeVal[-2]):
        x1 = round((lowerRoot+greaterRoot)/2,3)
        print(f"x{(len(storeVal)+1)} = ({lowerRoot} + {greaterRoot}) / 2 = {x1}\n")
        check = findAlgeRoot(x1)
        if(check < 0):
            lowerRoot = x1
        elif(check > 0):
            greaterRoot = x1
        storeVal.append(x1)
    print(f"Your answer getting into x{len(storeVal)} iteration")
    print(f"x approximate | {storeVal[-1]}")

def findAlgeRoot(i): # this is the findRoot function which provide root using
                 # equtions.
    val = round(((i*math.exp(i))-3),7)
    if(val > 0):
        print(f"f({i}) = {i} * e^{i} - 3 = {val} ... {val} > 0\n")
    elif(val < 0):
        print(f"f({i}) = {i} * e^{i} - 3 = {val} ... {val} < 0\n")
    return val

'''print("\nLet, f(x) = x-cosx \n")
j = 1   # Declare variable and empty list
val = []; # This is the list where all root are store
i = 0
while(not val or True): # The loop continues until a greater root is not found.
    val.append(findTrigoRoot(j))
    if(val[-1] < 0):
        i += 1
    elif(i > 0 and val[-1] > 0):
        break
    j+=1
    
print("\nso, Root lies between ",j-1," and ",j,"\n")

findAlgeRootValue(j)'''

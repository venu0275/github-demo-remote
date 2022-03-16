# Add implementation
def add(x,y):
    return x+y

# Subtract implementation
def subtract(x,y):
    return x-y      # implementation on master branch

# multipy implementation   
def multiply(x,y):
    return x*y      # on Bug456 branch

# divide implementation   
def divide(x,y):
    if y==0:        # on master branch
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
#Square implementation
def square(x):
    return x*x
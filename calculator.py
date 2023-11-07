# Design a simple calculator with basic
# arithmetic operations. Prompt the user
# to input two numbers and an operation
# choice. Perform the calculation and
# display the result.

#functions
def add(x,y):
    return (x+y)

def sub(x,y):
    return (x-y)

def multi(x,y):
    return (x*y)

def div(x,y):
   return (x/y)

def exp(x,y):
    return (x**y)

def rem(x,y):
    return (x%y)


a=input("Enter a number :")
b=input("Enter a second number :")

if a.isdigit():
    a=int(a) 
else:
    print("choose a digit:")


if b.isdigit():
   b=int(b) 

else:
    print("choose a digit:")



user_choose=input("What do you want to do add,subtraction, multiplication,division,exponential,reminder:\n(add,sub,multi,divi,expo,rem);")

if user_choose=="add":
    print(a,"+",b,"=",add(a,b))

elif user_choose=="sub":
    print(a,"-",b,"=",sub(a,b))

elif user_choose=="multi":
    print(a,"*",b,"=",multi(a,b))

elif user_choose=="divi":
    if a<=0 or b<=0:
        print("please enter a number which is greater than zero")
    else:
        print(a,"/",b,"=",div(a,b))

elif user_choose=="expo":
    print(a,"**",b,"=",exp(a,b)) # 2**2=4 || power(2,2) || 2^2

elif user_choose=="rem":
    if a<=0 or b<=0:
        print("please enter a number which is greater than zero")
    else:
        print(a,"%",b,"=",rem(a,b))

else:
    print("Please choose correctly:)")
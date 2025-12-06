#Syntax error just must be fixed , other errors are like runtime error for which we can have defenses 
#we have try and except for this 

try:
    x = int(input("What is x? ")) #here if we type character we will have a valueError 
except ValueError:                  #when valueerror is raised print the following 
    print("x is not an integer")

#try is only working on the int input line not the print line therefore print(x) need not to be inside the try scope 
print(f"x is {x}")
#but when we now give the input as a character there is a name error that x is not defined beacause when valueerror trigerred in int input no value was copied into x therefore x does not exist yet
#but this can be fixed with else

try:
    z = int(input("Enter the number z: ")) #if somethig goes wrong go to exception otherwise continue with else block 
except ValueError:
    print("z is not an integer")
else:
    print(f"z is {z}") 

def getint():
    while True:
        try:
            b = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number")
        else:
            return b 


r = getint()

def get_int():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a number") 

get_int() #we also can have that we pass inside the exception and return to the try statement in the loop , we catch the execption but dont show it 


def get_inti():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass

get_inti() #we also have a finally clause that runs everytime even on error and it runs before returning control to try 


def final():
    try:
        h = int(input("Enter number: "))
    except ValueError:
        return "ENter valid"
    else: 
        return "Good"
    finally:
        print("Still executes")

final() #the finally clause executes first and the others inwhich we have return values execute later 

def zero():
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            print(x/y)
        except ValueError:
            print("Enter valid integer")
            return zero()
        except ZeroDivisionError:
            print("Division by zero not possible")
            return zero()
        except ValueError as e: #to catch any other errors 
            print("Error: ",e)


zero()

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("You tried to divide by zero!")
    return x / y

print(divide(10, 2))  # works fine
print(divide(10, 0))  # raises ZeroDivisionError


o = int(input("Enter o: "))
assert o>0 , "o must be positive " #this will raise an assertion error D
#def is used to define our own functions 
def greet():
    print("Hello")
#functions can be moved to laast part in code to keep clean 
#we use main here to denote that this is the main function and call it at last after defining out function =s 
def main():
    hello()
    name = input("Whats your name? ")   #the scope of name is main 
    hello(name)#passing the input name variable as an argument. When function is called the name is copied to "to" inside the function 
    x = int(input("What is x "))
    if iseven(x):
        print("The number is Even")
    else:
        print("Odd")
def hello(to= "world"): #default value , if user doesnt give input, print hello world when function is called 
    print("Hello", to)

#main() #calling the main function after defining all the defined functions

def calc():
    x = int(input("What is x "))
    print("x sqaured is", square(x))

def square(n):
    return pow(n,2) #return value of the function 

def iseven(n):
    if n%2 == 0:
        return True
    else:
        return False

main()

def cat():
    x = get_input()
    meow(x)

def get_input():
    while True:
        n = int(input("What is n? "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("Leow")

cat()


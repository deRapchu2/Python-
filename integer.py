# int , we have arthematic operations on them , % modulo ,  a function 
# in python we have interactive mode that is running python in terminal it will execute each line we write immideiately 
# #running arthematic is easy there
x = input("X = ") #this is stored as a string by default for input() function 
y = input("Y = ") #now we will type cast 
z = int(x)+int(y) #adds two strings to each other , concatenating without specifyinh int 

print(z)
x = int(input("Enter x ")) #here in function nesting the return value of first function becomes the argument to second function 
y = int(input("Enter y ")) #converts the string taken as input into integer , input(int) , is saying convert the integer function into input which doesnt mean anythin
print(x+y)
#we also have float , a real number ,
x = float(input("Enter x ")) 
y = float(input("Enter y "))  
print(x+y) 
#to round to the nearest integer we have round and its syntax is round(number[, ndigits]), number of digits to round off to 
print(round(x+y))
print(f"{round(x+y): ,}") #here we add , to aftere every hundreds place 

z = round(x/y , 2) #rounding off to 2 decimal places 
print(z)
print(f"{(x/y): .2f}")#this is also the way to round off to two decimal places 

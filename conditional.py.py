#comparing values 

t = int(input("Enter t: "))
i = int(input("Enter i: "))

if t < i: #this is a boolean expression because only two possible answers 
    print("t is less than i")
elif t>i:                           #if one of the statements here executes the conditional exits 
    print("t is greater than i")
else:                               #this is the default if all other conditionals fail
    print("t is equal to i")

if t<i or t>i:
    print("t is not equal to i")
else:
    print("t is equal to i")


#module that will give acess to value typed at command line that is sys , most specifically sys.argv , argument vector at command line 
import sys 


try:
    print("Hello , my name is", sys.argv[1]) #argv[0] stores the name of the code , if we dont give argument at command line it will show IndexError
except IndexError:
    print("Please provide an argument") #for full name cover in ""
#this can be replaced by '
if len(sys.argv) <2:
    print("Two few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("Hello, my name is", sys.argv[1]) #this is inefficeint because the actual code is only the last , or in else 

#we can do 
if len(sys.argv) <2:
    sys.exit("Two few arguments") #exit the code no further checking
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("Hello, my name is", sys.argv[1]) #here the two exceptions are checked early and sys.exit is called therefore by this line there are no erros and can be executed without an else 

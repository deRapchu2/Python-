#Introduction to programming to python 

#Function and variables , week 0 

print("Bye, world!")

#pyhton is name not only of the language but also the interpreter
#a function is like a action or a verb that the language already know what it deos , like print is a function 
#argument is the input to that function an it will produce a side effect 

#Now to give input 

print("Whats your name ? ")
input("Whats your name? ") #this takes string as input from the standard librabry 

#this input also has a return value which is a string which we can use to print in a print statemenet 
#to store this return value we can use a variable 

name = input("Whats your name? ") #= the assigment operator , copies the return value of input function into name variable 
#now to print that value stored inside the variable 

print("Hello ,")
print(name) #"" , not assigned because not to print the "name" as a string 

#this prints the name variable on the next line 

# """" This is a multiline comemnt """" 
name2 = input("Race: ")
print("hello, "+ name +name2) #this adds the input string to the string we print using print , one argument using concatenation
print("Hello,", name, name2) #argument to print seperator is comma , and this adds a spaces between comma of hello and the name  , three argument

#the print is automatically moving the cursor to next line \n , to prevent this we can do 
#in the documentation of print there is print(*objects ,  sep = ' ', end= '\n' , file = sys.stdout , flush = False) , end here can be edited 

print("Salam ,", end = "") #override the basic end and make end as nothing so new print prints in the same line 
print("Good morning,", end = "Dearest ")#make the string input end with dearest
print(name)
print("hello,", name , sep = 'Whateber') #these are named parameters , here the seperator 'space' is replaced by whateber
#printing quotes 
print('hello, \"friend\"')

print(f"sasrikikaka , {name}")#tells python to format this string , formatted printing 

#All this time we have been hopeful of the user input to just be a string but it can be otherwise , , or a proper string 
#example lower uppercase and accidental spaces , example giving inout to input string as '     falaan   ' it will print spaces too after greeting

name = name.strip() #removes whitespace from the string left and right not between, strip here is a function or more precisely a method , returns that to name 
print(name)#while storing names we also want to capitalise 
name = name.capitalize()
print(f"naah , {name}") #but this only capitalizes first letter of the string not first letter of each word 
name = name.title()
print("hello", name)

print("Yamai kudasai, ", name.strip().title(), "san", sep = " ", end = '\n') #this can be done at input().strip().title() , there are also lstrip and rstrip 
name = input("Enter your name: ").strip().title()
#there are also methods in string =s which can be used to store the long string containing spaces into muktple strings storing words and 
#that cna be used to for example greet a person by their first name only 

#Splitting users name into first name a last name 

firstname , lastname = name.split(" ") #giving more will raise an execption 
print("Yello,", firstname)

#int string and float are immutable therefore any change creates a new object in the memory 

x = 10
print(id(x))
x = x + 5
print(id(x)) #we can see here that x just now points to a different location 

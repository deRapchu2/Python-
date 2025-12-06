print("Meow")
print("Meow")
print("Meow") #Here we are doing repetition therefore we can automate this with loops 
#we can also use multiplication for string multiply 
print("meow"*3) #this prints meowmeowmeow as it joins string continously 
print("meow\n"*3 , end = "") #end specified becuase python automatically does \n so the an extra line is printed because of both our \n and pythonss therefore we replace it here 

i = 3
while i >1:
    print("Meow!")
    i -= 1
    
x = 0 

while x <1:
    print("Weow")
    x += 1 

for i in [0,1,2]: #for is usually used for list iteration #this is a list , [] represent a list
    print("Teow")
#what if there are millons itereations needed therefore it can be done by 
for k in range(6): #no need to initialize the a previously to use it , 6 automatically means 0 to 6 that is 0,1,2,3,4,5 in a list
    print("jeow")  #here the itereation happens upto the number but not through  the number we specify 

#as here the k variable is just used by python for iteration and not useful to us therefore it is named "_" to denote that it is not being used in code anywhere 

#asking user input for number of meowing , we have to prevent negative inputs 

l = int(input("Enter the number: "))

if l <0:
    l = int(input("Enter the number: "))
    if l <0 :                           #enters a negative value second time 
        l = int(input("Enter the number: "))
        if l<0:
            l = int(input("Enter the number: "))
    else:
        print("Ok")
            
#this will have to go on forever to check again and again , but we have this , when we want an user input that matches a certain expectation we can do 

while True:
    n = int(input("Enter the digit: "))
    # if n <0:
    #     continue #continue the loop
    # else:
    #     break this can be replaced by 
    if n>0:
        break 

for _ in range(n):
    print("JJJJJJ")


#making function for all this 

def main():
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

main()
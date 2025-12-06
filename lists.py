# a list is created as following , can take set ,tuple , dictionary as arguments 

my_list = ["hello", "world", "my","name",'is','kamala']

num_list = [1,2,3,4,5,6,7]

mix_list = [1,'werer', 90 , 'kereala',True]

nested_list = [['hello', 'world'], ['byewerwere', 'world'],['bi', 'eee'], ['a','z'],['a','b']]
nested_num = [[1,2,3], [4,5,6],[7,2,0],[0,0,0],[3,56,98],[7,1,0]]

print(nested_list) #this is different from a matrix because different data type and maths cant be done on it 
#just list inside a list 

#print(nested_list[1,1]) this wont work because we are passing a tuple the correct format is passing one level at a time

print(nested_list[1][0]) #indexing of a list 
print(num_list[2:4]) #elements 2 to 4 leaving 4 
print(num_list[::2]) #start to end with 2 steps each , step slicing 

#some of the functions regarding lists are 
len(my_list) #returns an integer as length of list 

max(num_list) #will not work for mix , in case of nested returns first element of the list
#and will return the string with maximum ascii value for a string list 
#max of a nested numerical will return element with greatest first element 
min(my_list) #has the same behaviour 
sum(num_list) #will not work on any other 

sorted(nested_num) #it checks the first element for sort if they are equal than the second element and the following
#this also sorts string lists by the ascii value same for nested string lists and works simillarly for nested strings
#returns a list

#we can also pass a string to a list and it will store it character by chracter , list(iterable)

list("functions are ok") #only takes one argument , not numbers 

#METHODS on lists 

my_list.append("makkker ") #takes one argument and appends to the end of the list , can take a list too 

num_list.extend([55,44,33,22]) #takes multiple arguments , same as append but here we have multiple argumenets 
#but they have to be passed as a list or other single daata type , doing same in append will add a list not elements

my_list.insert(1,"Worlds") #insert "Worlds" at index 1 of my list , insert takes integer argument no list tuple 
#giving big indexes just appends value at end of the list doesnt create a large index 
#giving large negative index appends the value to the start 
nested_list[1].insert(0,"byees") #specify first for nested ones 

my_list.remove("hello") #remove(x) , x should be present inside the list , starts to remove from the beginning , removes first match
#and one works one time on only one element 
while True:
    num_list.remove(7)
    if 7 not in num_list:
        break #this will remove all the instances of 7 from the list 

my_list.pop(1) #give in range the index which has to be removed and returned , takes only one argumen

num_list.clear() #takes no arguments and clears the list , workds on lists not integers and strings  , can also be used for nested ones 

num_list.index(1) #returns the index of first match , list can be passed 
num_list.index(1,5,14) #search for 1 starting from index 5 to index 14 , end can be as big or can be left empty to go to the end 

my_list.count("hello") #takes an integer or a string literal and returns the number of times it occurs in a list 

nested_num.reverse() #takes no arguments and reverse the entire list 

num_list.sort() #sort the string and return it in ascending order ,this takes reverse and key also as parameters 
#the key is used to pass a function to sort and on the basis on return value of the function on each element in list , sort the list 

new = nested_list.copy() #returns a shallow copy of the list 
b = nested_list #this is a reference not a shallow copy

#OPERATIONS on list 
nested_list + nested_num
(nested_list)*3
2 in [1,2,3] #returns true 

[round(x) for x in [1.2,2.3,3.4]] #[fuction (x) for x in [............]] mapping a function onto a list 

del my_list[0:3]

#get unique elements in a list 
list(set(num_list))

#flatenning a 2d list 
flat = [x for sub in nested_list for x in sub] #For each sub-list inside nested_list,
#take each element x from that sub-list,and collect it into a new flat list
#same as 
# flat = []
# for sub in nested_list:      # 1️⃣ take each inner list
#     for x in sub:            # 2️⃣ take each element in that inner list
#         flat.append(x)
#filter 

[x for x in num_list if x > 5 ]





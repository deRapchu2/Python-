#tuples are ordered , hashable and immutable collection of items 

tup = (4,1,2,1,1) #ordered means that items have fixed positions and can be accessed like in lists 
#allows duplicate items unlike sets 
print(tup) 

tup2 = (2,3,'abc', [4,5], {"hello", "World"}) #the inner list can be changed but not the tup2 
print(tup2)

tup3 = tup + tup2 #adding one tuple to another , concatenation
nestedtup = 1,2,3,"h","reeel", (3,2,11), ["killer", 45]
tup4 = tup3*2 #two of these tuples inside the tup4 
print(len(tup4))
3 in tup #memebership , true if 3 is present inside tup 
#this below is known as packing , turning elements into a tuple 

t = 1,2,3,4,"333" #if we check the type here it will be tuple by default 

#For a single element tuple we must add a comma otherwise it will be interpreted as int or string 
a  = 5 #this is an int
a = 4, #this is a tuple 
type(a) #prints tuple

#ACCESSING ELEMENTS OF A TUPLE 
#exactly how we find in lists 
#tuple slicing below 
tup[1:3] #second element and third element leaving the forth and further
tup[-1] #last one  
nestedtup[5][1] #acessing nested tuples 

nestedtup[6][1] = 33 #changing the element of mutable list inside the immutable tuple

#Unpacking of tuple 
#here unpacking refers to storing each element of the tuple inside a new variable 

p = (2,45,2,3,4)

a,b,c,d,e = p
print(a)

#METHODS ON TUPLES 

#there are only two inbuilt methods count and index 

p.count(2) #count of element x inside tuple 
p.index(2) #index of element x inside the tuple , returns the first match 

#trying to change a tuple will throws a type error 
tup[1] = 2 #TypeError: 'tuple' object does not support item assignment

#SInce tuples are immutable and hashables therefore they can used as keys in dictionaries 

marks = {(44,13): "Naher", (55,33):"Laher"}
print(marks[(44,13)]) #Value at key 

lisst = [1,2,3,4]

tupple = tuple(lisst) #converting a list into a tuple ,tuple() creates new immutable copy 

lst = [1, 2, 3]
t = tuple(lst)   # makes a NEW immutable copy , here the changed will not reflect if made to lst 

lst.append(4)
print(lst)  # [1, 2, 3, 4]
print(t)    # (1, 2, 3)

lst = [1, 2, 3]
t = lst,   # the tuple contains the actual list object , contains list as object 
#and changes made to the list will reflect here 

lst.append(4)
print(lst)  # [1, 2, 3, 4]
print(t)    # ([1, 2, 3, 4],)

result = tuple(2* item for item in tup)
result  #multiplying each element by a scalar
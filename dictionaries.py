#A dictionary stores data in key value pairs 
#dict = {key : value} this is the format used 

W = {1,2,3,4}
S =  frozenset(W)

person = {
    'Name' : 'Helo',
    'Age' : 45,
    "city" : "Baramulla",
    ('MArks', 'Science') : 45,  #the keys must be unique otherwise problems in value access 
    S : 45,
    50 : "Naahh", #values may be same for different keys and can be anything 
    "dict" : {"key":"VAlue"},
    "Set" : {1,2,3,4},
    "list" : ["hello"],
    3.14 : "pi"
} #the keys are immutable therfore can be tuple , int , float string etc 

#to access values inside of keys or at keys we have 

person["Name"] #dictionary name followed by name of the key
person[50]
person["dict"] #if a key doesnt exist it will throw or raise a key error 

#we also can do safe access to mitigate the error if present by doind 

person.get("salary") #will return none if doesnt exist no error raised however

person.get("Month" , 0) # if month doesnt exist will return 0 as default 

#therefore what dict['not_present'] is doing by default is 

person.get("salary" , KeyError) 

#Adding or updating entries 

person["Age"] = 33 #updating the age to be 33 , can be updated to a string also 
person["Age"] == 33 #a bool that will return true 

person["Month"] = "Whatever" #adding a new key value pair or an entry 

person.get("Age") = 44 #this will not work because this function call cannot be 
#assigned a value only checks and returns default as specified 

#Removing entries 

#for removal we have various methods that can be performed on the dictionary 

person.pop(50) # will remove the key and return its value example 

t = person["dict"].pop("key") #t will store "VAlue" , this can also be done as 

u = person.get("dict").pop("key") #from persons get dict and inside that pop and return

person.popitem() #removes last inserted pair takes no arguments and returns it as tuple

#to delete the key and no return we have 
del person[50] 
del person["dict"]['key'] #this to delete nested elements 

#to empty out the dictionary we have 

person.clear() 

#VIEWS of a dictionary , change when dict changes automatically 

person.keys() #return a set like object of keys , dict_keys([x,y,z]) ,  dict_keys method 

person.values() #return object providing view of values 

person.items() #returns set like object of key value pairs as a tuple 
len(person) #total number of items 
#Looping through a dictionary , default looping here gives us keys 

for word in person:
    print(word)  #this will return keys of the dicntionary 

for defintions in person.values():
    print(defintions)

for (word , defintions) in person.items():
    print(word , defintions) #this will loop over and return the key value pairs 

for items in person.items():
    print(items) #this will return them as tuples 

#to check membership 

"Name" in person #will return true , but only for keys , for values we have 
"Helo" in person.values() #this is also true 

#Dictionary comprehension 

table_of_3 = {f'3 X {x}' : x*3 for x in range(1,11)}  #first key than value 

#Renaming can be done by creating variable that will point to the same id 

new_person = person 

#To copy (shallow) a dictionary 

new = person.copy()

#Merging two dictionaries 

person.update(table_of_3) #if there are same keys than value of the key from 
#the dictionary given as argument will override the dictionarry on which method is performed

#To update a key / change its name we can do 

person["NAME"] = person.pop("Name")

#this can also be done by 

person["NAME"] = person['Name'] #copy the value in Name into NAME  
del person["Name"]  #delete Name entry  , both of these will append to the end of the dictionary 

#IF we equate the keys as a = b than value of b is copied into a 
#If value is immutable → safe copy
#If value is mutable → they share the same object ,as if we equate a list object than .append will effect both

dict1 = {"a": 1, "b": 2, "c": 3} #for renaming we can also do 

dict1 = { (k.upper() if k == "a" else k) : v for k, v in dict1.items() } #changes a to A 

#to rename all keys to strings we have 

dict1 = {str(k): v for k,v in dict1.items()} 

#ADVNACED DICTIONARY FUNCTIONS 

from collections import defaultdict , Counter 

#default dict is used when we try to access a key that doesnt exist , it automatically creates it with a 
#default value , defaultdict(x) , x is the function that tells defaultdict what default value to create

f = defaultdict(int) #int returns zero therefore f['a'] will have value 0 


def three():
    return 3
f = defaultdict(three)
f['h']  #this will return 3 


t =  defaultdict(str)
t["new"] #creates an empty string at the value as ''
t["new"].capitalize() #string methods can therefore be performed on these default strings inside the dict


d = defaultdict(list)
d["a"].append(10)    # works even tho "a" didn't exist , {'a': [10]} is created 

#for having defaults other than 0 , empty strings or empty list we can use lambda as 

l = defaultdict(lambda : 10) #integer defaultdict with default value for each key as 10 
o = defaultdict(lambda : "Hello, ") 
p = defaultdict(lambda: [0]) 
#this can be used in various ways such as 

count_of_z = defaultdict(int)

for char in 'why this zigga':
    if char == 'z':
        count_of_z['z'] += 1 #create a dictionary entry key as z and increment it if z appears as out in if
    
count_of_z
#also can be used as 

counts = defaultdict(int)

for char in "okaaaaayyyy lets go":
    counts[char] += 1 #counts each character 
counts
#it can also be used for grouping items such as 

group = defaultdict(list)

pairs = [("fruit", "apple"), ("fruit", "mango"),
         ("car", "BMW"), ("car", "Audi")] #created a list with tuples 

for k,v in pairs:
    group[k].append(v) #group is dictionary in which the default is list therefore this method is applied 
                        #create an entry group[k] and append it v , (k,v) from the pairs 
                        #group[k] create the key and in the empty list append v 

#We can have nested default dictionaries as 

j = defaultdict(lambda: defaultdict(int))
j['X']['Y'] = 10 

#in default dictionaries we cannot prepend to the first position for that we have ordereddictionaries 

from collections import OrderedDict

k = OrderedDict({"a": 1, "b": 2, "c": 3})
k.update({"FIRST": 999})
k.move_to_end("FIRST", last=False)   # move to beginning
print(k)

#We also have counter that is used to count each element and store it as a dictionary 

numbers = [1,2,3,3,4,5,3,5,7,5,46,4,6,4,3,2,5,8,9]

c = Counter(numbers) #c is a dictionary now 

c.most_common(1) #list the most common(n elements)
c.total() #returns total number of items 

#Sorting a dictionary 

#if the data type of keys is same or atleast comparable than they can be compared as 

sorted_dictionary = dict(sorted(dict1.keys())) #this will sort keys 

#different types can be sorted only if the we convert all to some data type as :

sorted_dictionary = dict(sorted(dict1, key= str)) #if this inst possible than we do 

sorted_dictionary= dict(sorted(dict1.items(), key = lambda x:x[1])) #but this will only compare values not keys
#here also values must be comparable ,compare by each value x , which is a tuple , x[1] therefore by values  
#at the end of this we can give reverse = true also 

#COnverting dictionary to json string 

import json

data = {"name": "Ali", "age": 21}
json_str = json.dumps(data)  # dict → JSON string
print(json_str)

dict_back = json.loads(json_str)  # JSON string → dict
print(dict_back)

students = ["Hermaine", "Harry", "Ton", "Draco"] #list of length 3 
houses = ["Griffindor","Griffindor","Griffindor","slytherin"]
print(students)
#printing a value from list

print(students[0]) #indexing into the list , the lists are zero indexed 
print(students[1])
print(students[2])


#this is same as 
for s in students:   #this time we are using the variable to iterate automatically over the list students 
    print(s) #this only happens in pythhon 

for i in range(len(students)): #length of a list is returned to i as integer for number of iterations , returns a list of [0,1,2] for i to get assigned as 
    print(i+1,students[i])

print(students*2) #prints students twice 
print(students + houses)
#dictonaries in python are a data structure that allow us to associate one value to another , or a key to a value , word and definition , maps keys to values 
#it relies on hash tables , "name" has hash 1123 and "Zaid" is at index 3 , maps the hash to a postion (index) in an internal array
#hash is just a location in memory or a number produced for a location in memory 

#for exaample keeping track who lives where , or accessing them where they live by their name 

Students = {"Heromoine": "Griffindor",
            "Harry": "Griffindor",
            "Ton": "Griffindor",
            "Draco": "Slytherin",}
                                                #as lsits have indecies here in dictionary the index can be words as well and not numeric
print(Students["Heromoine"])    #indexing into the dictionary ,[] for indicies, gives the value at the index 
print(Students["Harry"]) 
print(Students["Ton"]) 
print(Students["Draco"]) 

for index in Students:        #here we will see the keys , a for loop iteratingover a dictionary iterates over the keys 
    print(index)              #a string

    #now to print who lives where 

for key in Students:
    print(key , Students[key], sep = ", ")  #using the key to index into the dictionary 
#A set is a mutable , which can be changed , unordered and unique collection of elements 

my_set = {1,2,3,44,5,7,0,7,7,44} #no duplicate values and no defined order , elemeents must be immutable ,
#cant be list ot dicts , {} is using a set literal , sets are unidexed 

print(my_set) #even if there are repeated elements thte set will be always printed only of the unique values 

s = set([1,2,3,4,4,44,2]) #another way to declare set , using a constructor , passing a string literal
#tells pyhton to convert this string literal to set elements 
print(s)

z = set()
print(z)

l = set({"hell":"worlds", "jaja":"kakak"}) #this set will only print the keys and not the values 
set((1,2,3))
set("abc") #passing to the function call a string , each letter is stored seperate
set({1,2,3}) #a set function call taking set as an argument
set(range(3,10,2))
#set(set) this does not work because a set can only contain hashable (immutable) objects , since 
#a set can be changed therefore its not hashable therefore cant take set as an argument
#set() can take mutable iterables (like lists) as arguments,
# but the elements inside the set must themselves be immutable.
#for set inside a set we have to use a frozenset 
f = frozenset([1,2,3,4])
new_set = set(1,2,3,f,5,6)

#METHODS on sets 

my_set.add(54) #adds 54 to the end of the set 
my_set.update([43,22,11]) #adds multiple elements to the set 
my_set.update({'b'})

my_set.remove('b') #element must be a member of the set else raise keyerror (mapping key not found)
my_set.discard(4) #removes 4 , no error if missing 
my_set.pop() #returns an integer , no argument , pops out a random element from the set 

l_set = my_set.copy() #shallow 
p_set = my_set #reference 
l_set.clear() #retuns none takes no argument and clear the set , return set()

#SET OPERATIONS 

A = {1,2,3}
B = {3,4,5}

A.union(B) #UNION of both sets 
A.intersection(B) #intersection of both sets 
A&B #intersection of both sets 
A-B #difference of both sets or 
A.difference(B)
A^B #symmetric difference 
A.symmetric_difference(B)

2 in A #returns True 

for i in A:
    print(i) #print members of the set 

#SET RELATIONS 

A <= B #is A a subset of B or is  A present in B ?
A.issubset(B)
A < B #is A a proper subset of B or is A whole of A present in B and B has more ? Equal sets can be subsets 
#but not proper subsets 

B >= A 
B.issuperset(A) #does B contain all the elements of A 

A.isdisjoint(B) #reteurn true if A and B have no common elements 

my_list = [1, 2, [3, 4]] #converting this mutable list to immutable tuple and storing it inside a set 
converted = [tuple(x) if isinstance(x, list) else x for x in my_list] #if returns true if x is a list 
print(set(converted))

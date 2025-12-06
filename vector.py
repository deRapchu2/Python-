# A vector is reoresented as an ordered tuple 

v1 = (4,3) #4 in x and 3 in y 
v2 = (1,2)
#dot product without numpy 
#if >0 than vectors are same direction , <0 opposite , =0 perpendicular or orthogonal 
dot = v1[0]*v2[0] + v1[1]*v2[1] 
print(dot)
result = tuple(2* item for item in v1) #scalar multipplpication of a vector stored into a new 

#vector lead directly into matrices and here we can use library numpy,numerical python,for all these operations

import numpy as np

v3 = np.array([1,3,7])
v4 = np.array([4,3,7])

print(np.dot(v3,v4)) #dot product of both

#cross product exists for 3d vectors and are done by matrix multipplication and top row being i , j ,k 

#cross product = 0  means that vectors are parallel otherwise a cross product returns a resulting vector 

print(v3+v4) #addition of vectors , addds each element to the corresponding element ,only works if shape is same

print(v4 - v3) #subtraction of vectors , v4[0] - v3[0] , v4[1] - v3[1]  , v4[2] - v3[2] 

#to calculate the magnitude of a vector we have the function 

np.linalg.norm(v3) #returns np.float64(result)

#Now to calculate the direction or unit vector we have 

Unit_v  = v3/np.linalg.norm(v3) #dividing the vector by its length to get the direction 

#Now to calculate the angle between them , cosX we have the formula 

cos = np.dot(v3,v4)/(np.linalg.norm(v3)*np.linalg.norm(v4)) 

#to calculate projection of v3 on v4 we have , a shadow of vector over another done to see its effect, |v3|cosX

proj = (np.dot(v3, v4) / np.dot(v3, v3)) * v3 #used in gps for shortest path and used in sports analytics 

#Linear combination 

# A vector C is said to be linear combination of vector A and vector B if C = xA + yB , x,y belong to R

x = 3 
y  = 2 

C = x*v3 + y*v4 
print(C)

#TWo vectors are linearlly independent if their determinant != 0 , det is [[a1 b1] , [a2,b2] ] 

#MATRIX VECTOR MULTIPLICATION 

# a matrix z represents a transformation
mat = np.array([[1,2],[3,4]])
vec = np.array([1,2])

z = mat @ vec #this does mat⋅vec=[ax+bycx+dy​] , vec = [x,y] and mat = [[a,b],[c,d]]

#this is core to neural networks where output=W⋅input+b , where W is matrix and input is a vector , b is bias


#if two vectors are not orthogonal therefore there is a compoenent or projection of one on another 
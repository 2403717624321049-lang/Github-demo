#Numpy - Numerical python
import numpy as np

#creating a 1d array
a=np.array([1,2,3,4,5])
print(a) # list without commas
type(a) #datatype - numpy.ndarry

#creating a 2d array 
b=np.array([(1,2,3),(4,5,6)])
print(b)
''' to specify Data type '''
c=np.array([(1,2,3),(4,5,6)],dtype=float)
print(c)

#placeholders ones , zeeros

d=np.zeros((4,4))
print(d)
e=np.ones((3,3))
print(e)
f=np.full((2,2),7)
print(f)

#create an identity matrix 
g=np.eye(3)
print(g)

# matrix- array wit random values
''' 1. random floats'''
h=np.random.random((4,5))
print(h)

'''2. random integers with a specified range''' 
i=np.random.randint(10,100,(4,4))
print(i)

#evenly spaced array 
j=np.linspace(10,30,12) # 12 - represents total no of values needed
print(j)

#evenly spacing with a step value 
k=np.arange(10,30,5)
print(k)

# changing datatype 
list1=[1,2,3,4,6]
l=np.asarray(list1)
print(l)

#Analysing a numpy array
print(c.shape) # dimension of the array/matrix
print(a.ndim) # no of dimensions in the matrix
print(j.size) # no of elements in the array 
print(l.dtype) # datatype of the array 

#Math operations


'''
Created on May 2, 2019
Numpy tutorial
@author: subharad
'''
import numpy as np

a = np.array([1,2,3]) 
print(a)

a = np.array([[1, 2], [3, 4] , [5,6]]) 
print(a)

a = np.array([1, 2, 3,4,5], ndmin = 2) 
print(a)

a = np.array([1, 2, 3,4], dtype = complex) 
print(a)

my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

print(my_array)

print(np.ones(2, dtype = np.int32))
print(np.zeros((3,2,3),dtype=np.int16))
print(np.ones((3,2,3),dtype=complex))
print(np.random.random((2,4)))
print(np.empty((3,2)))
print(np.full((2,2),3))
print(np.arange(10,25,2))
print(np.linspace(0,2,4))

'''
x, y, z = np.loadtxt('C:/Users/subharad/Desktop/data.txt',
                    skiprows=1,
                    unpack=True)

print(x,y)
'''

x, y, z = np.genfromtxt('C:/Users/subharad/Desktop/data.txt',
                       skip_header=1,
                       filling_values = 290,
                       unpack=True)

print(x,y,z)
my_array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)

print(my_array.ndim)
print(my_array.size)
#print(my_array.flags)
print(my_array.itemsize)
print(my_array.nbytes)
print(len(my_array))
x = np.ones((3,4))
print(x.shape)
'''
y = np.random.random((3,4))
print(y.shape)
print(x+y)
'''
y = np.arange(4)
print(x)
print(y)
print(y.shape)
print(x-y)
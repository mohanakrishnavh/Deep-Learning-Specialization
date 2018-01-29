# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 19:34:37 2018

@author: Mohanakrishna
"""

import numpy as np

print("Inconsistent Implementation")
a = np.random.randn(5)
print(a)
print(a.shape) #rank1 array - neither a row nor column vector
print(a.T)
print(np.dot(a,a.T))


#Correct way of defining the random vector - avoiding rank1 vector
print("Consistent Implementation")
a = np.random.rand(5,1)
print(a)
print(a.T)
print(a,a.T)

'''
If unsure of the shape throw an assert statement
assert(a.shape ==(5,1)) - Inexpensive check

If you still end up with rank1 array, it can be reshaped
a = a.reshape((5,1))
'''

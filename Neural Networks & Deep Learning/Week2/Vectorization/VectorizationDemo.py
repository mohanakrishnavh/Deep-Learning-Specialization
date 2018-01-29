# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 11:33:22 2018

@author: Mohanakrishna
"""

import time
import numpy as np

#Numpy array
a = np.array([1,2,3,4])
print(a)

#Vectorized version
a = np.random.rand(10000000)
b = np.random.rand(10000000)
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print("Vectorized version: "+str(toc-tic)+" ms")

#Non-vectorized Version
c=0
tic = time.time()
for i in range(10000000):
    c+=a[i]*b[i]
toc = time.time()
print("Non-Vectorized(\"for\" loop) version: "+str(toc-tic)+" ms")

# -*- coding: utf-8 -*-
"""
2018/10/31 
Aapproximate the delta functions using window functions.

"""

import numpy as np
import matplotlib.pyplot as plt


T = 0.000001
x = np.linspace(-0.01,0.01,200000)
y_A = np.zeros(x.shape)   # (x.size) is the number of elements  Different from (x.shape). x is 1D so both are ok here.
y_B = np.zeros(x.shape)
y_C = np.zeros(x.shape)
y_D = np.zeros(x.shape)

for i in range(x.size) :
    if x[i]>(-T/2) and x[i]<(T/2) :
        y_A[i] = (1/T)
    else:
        y_A[i] = 0

y_B = 1/(2*T)*np.exp(-abs(x)/T) 
y_C = (1/(T*np.sqrt(2*np.pi)))*np.exp(-(x*x)/(2*T*T))
y_D = (np.sin(np.pi*x/T))/(np.pi*x/T)

plt.figure(figsize=(15,10))
plt.subplot(2, 2, 1)        
plt.plot(x, y_A)
plt.xlim(-0.01,0.01)
plt.xlabel("t") 
plt.ylabel("x1(t)") 
plt.title("Rectangular Pulse") 

plt.subplot(2, 2, 2)
plt.plot(x, y_B)
plt.xlim(-0.01,0.01)
plt.xlabel("t") 
plt.ylabel("x2(t)") 
plt.title("Exponential Pulse") 

plt.subplot(2, 2, 3)
plt.plot(x, y_C)
plt.xlim(-0.01,0.01)
plt.xlabel("t") 
plt.ylabel("x3(t)") 
plt.title("Gaussian Pulse") 

plt.subplot(2, 2, 4)
plt.plot(x, y_D)
plt.xlim(-0.01,0.01)
plt.xlabel("t") 
plt.ylabel("x4(t)") 
plt.title("Sinc Pulse") 

# save the figure
plt.savefig(fname = "HW3_T_0.000001.png", format = "png")

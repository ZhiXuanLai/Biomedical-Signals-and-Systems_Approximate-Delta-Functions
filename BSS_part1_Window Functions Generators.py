# -*- coding: utf-8 -*-
"""
2018/10/17
Generate window functions
"""

import numpy as np
import matplotlib.pyplot as plt



# (a) w1(t) = 1
x = np.linspace(-2,2,2000)
cond_a = [True if (i>-0.5 and i<0.5) else False for i in x]            
y_a = 1*cond_a

# adjust the size of the figure
# adjust the blank space between subplots
plt.figure(figsize=(10,7))
plt.subplots_adjust(wspace = 0.4 , hspace = 0.5)

plt.subplot(2, 3, 1)
plt.plot(x, y_a)
plt.xlim(-2, 2)  # to set the range
plt.ylim(-1, 1.5)
plt.xlabel("t-axis") 
plt.ylabel("w1(t)") 
plt.title("w1(t) = 1") 


# (b) w2(t) = 1 − 2|t|/τ
cond_b = [True if (i>-0.5 and i<0.5) else False for i in x]            
y_b = (1-2*abs(x))*cond_b

plt.subplot(2, 3, 2)
plt.plot(x, y_b)
plt.xlim(-2, 2)  # to set the range
plt.ylim(-1, 1.5)
plt.xlabel("t-axis") 
plt.ylabel("w2(t)") 
plt.title("w2(t) = 1 − 2|t|/τ") 


# (c) w3(t) = 0.5 + 0.5 cos(2πt/τ)
cond_c = [True if (i>-0.5 and i<0.5) else False for i in x]            
y_c = (0.5 + 0.5*np.cos(2*np.pi*x))*cond_c

plt.subplot(2, 3, 3)
plt.plot(x, y_c)
plt.xlim(-2, 2)  # to set the range
plt.ylim(-1, 1.5)
plt.xlabel("t-axis") 
plt.ylabel("w3(t)") 
plt.title("w3(t) = 0.5 + 0.5 cos(2πt/τ)") 


#  (d) w4(t) = t/τ + 1/2
cond_d = [True if (i>-0.5 and i<0.5) else False for i in x]            
y_d = (x + 0.5)*cond_d

plt.subplot(2, 3, 4)
plt.plot(x, y_d)
plt.xlim(-2, 2)  # to set the range
plt.ylim(-1, 1.5)
plt.xlabel("t-axis") 
plt.ylabel("w4(t)") 
plt.title("w4(t) = t/τ + 1/2") 


# (e) w5(t) = cos(πt/2)
cond_e = [True if (i>-0.5 and i<0.5) else False for i in x]            
y_e = (np.cos((np.pi*(x))/2))*cond_e

plt.subplot(2, 3, 5)
plt.plot(x, y_e)
plt.xlim(-2, 2)  # to set the range
plt.ylim(-1, 1.5)
plt.xlabel("t-axis") 
plt.ylabel("w5(t)") 
plt.title("w5(t) = cos(πt/2)") 


# (f) w6(t) = e^−0.5(t+τ/2)
cond_f = [True if (i>-0.5 and i<0.5) else False for i in x]            
y_f = (np.exp(-0.5*(x+0.5)))*cond_f

plt.subplot(2, 3, 6)
plt.plot(x, y_f)
plt.xlim(-2, 2)  # to set the range
plt.ylim(-1, 1.5)
plt.xlabel("t-axis") 
plt.ylabel("w6(t)") 
plt.title("w6(t) = e^−0.5(t+τ/2)") 




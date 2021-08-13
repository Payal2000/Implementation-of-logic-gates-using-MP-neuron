# -*- coding: utf-8 -*-
"""IMPLEMENTATION OF LOGIC GATES USING  MP NEURON.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_QRW1KG17JliGS7oDIiJQyRyi3U-Y_pD
"""

#Implement AND using MP neuron
import numpy as np

x1= np.array([0,0,1,1])
x2= np.array([0,1,0,1])
t= np.array([0,0,0,1])
y= np.array([0,0,0,0])

w1= float(input('enter value of weight 1'))
w2= float(input('enter value of weight 2'))
T= float(input('enter value of threshold'))

yin= (w1*x1)+(w2*x2)

for i in range(4):
    if yin[i]>=T:
         y[i]=1
    else:
        y[i]=0
   
print('target o/p is ',t)
print('Actual o/p is ',y)

if np.array_equal(y,t):
    print('Correct values of weights and threshold')
else:
    print("Incorrect values of weights and threshold, Rerun the program")

#Implement OR using MP neuron

import numpy as np

x1= np.array([0,0,1,1])
x2= np.array([0,1,0,1])
t= np.array([0,1,1,1])
y= np.array([0,0,0,0])

w1= float(input('enter value of weight 1'))
w2= float(input('enter value of weight 2'))
T= float(input('enter value of threshold'))
1
yin= (w1*x1)+(w2*x2)

for i in range(4):
    if yin[i]>=T:
         y[i]=1
    else:
        y[i]=0
   
print('target o/p is ',t)
print('Actual o/p is ',y)

if np.array_equal(y,t):
    print('Correct values of weights and threshold')
else:
    print("Incorrect values of weights and threshold, Rerun the program")

#Implement XOR using MP neuron
import numpy as np
x1= np.array([0,0,1,1])
x2= np.array([0,1,0,1])
t= np.array([0,1,1,0])
y= np.array([0,0,0,0])
z1= np.array([0,0,0,0])
z2= np.array([0,0,0,0])

w11=float(input('enter value of w11'))
w21=float(input('enter value of w21'))
w12=float(input('enter value of w12'))
w22=float(input('enter value of w22'))
v1=float(input('enter value of v1'))
v2=float(input('enter value of v2'))
T=float(input('enter value of threshold'))

zin1= (w11*x1)+(w21*x2)
zin2= (w12*x1)+(w22*x2)

for i in range(4):
    if zin1[i]>=T:
         z1[i]=1
    else:
        z1[i]=0
        
for i in range(4):
    if zin2[i]>=T:
         z2[i]=1
    else:
        z2[i]=0

yin= (v1*z1)+(v2*z2)

for i in range(4):
    if yin[i]>=T:
         y[i]=1
    else:
        y[i]=0


print('target o/p is ',t)
print('Actual o/p is ',y)

if np.array_equal(y,t):
    print('Correct values of weights and threshold')
else:
    print("Incorrect values of weights and threshold, Rerun the program")
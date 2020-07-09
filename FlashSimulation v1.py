# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:15:41 2020

@author: Matheus
"""

import numpy as np
import matplotlib.pyplot as plt

# Matrix max size
maxH = 100
maxL = 310

# MATERIALS LIST
AIR = 0
DISILICATE = 1
PLATINUM = 2

# Radius and Length for the matrix construction
RADIUS = 35
ELECTRODE_RADIUS = 2
LENGTH = 16

# Interpolation tipes
INTERPOLATION = "None"
'''INTERPOLATION = "bilinear"'''

# ODE conditions
DX=0.0001
DY=0.0001
alpha=5
DT = (DX**2)/(2*alpha)

# Obj to help with radius calculation
class circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def heatDiffusion(TOld, Compos):
    i = 1; j = 1;
    # Creates a new matrix where the value is True where the composition is the same as the center
    diffusion = Compos[i,j] == Compos
    
    # In the 3rd line multiply by 1 since True + True is not 2, but True
    ResiduoX =   (diffusion[i+1,j]) * TOld[i+1,j]
    ResiduoX +=  (diffusion[i-1,j]) * TOld[i-1,j]
    ResiduoX -=  (1*diffusion[i+1,j] + 1*diffusion[i-1,j]) * TOld[i,j]
    ResiduoX /=  DX**2

    ResiduoY =   (diffusion[i,j+1]) * TOld[i,j+1]
    ResiduoY +=  (diffusion[i,j-1]) * TOld[i,j-1]
    ResiduoY -=  (1*diffusion[i,j+1] + 1*diffusion[i,j-1]) * TOld[i,j]
    ResiduoY /=  DY**2
    
    #Residuo = ((TOld[i+1,j]-2*TOld[i,j]+TOld[i-1,j])/DX**2)
    #Residuo += ((TOld[i,j+1]-2*TOld[i,j]+TOld[i,j-1])/DY**2)
    
    Residuo = (ResiduoX + ResiduoY) * DT
    return Residuo

# Create the Temperature and Composition matrix
temperature = np.zeros((maxH,maxL))
composition = np.zeros((maxH,maxL))

circle1 = circle(50,50)
circle2 = circle(50,260)
                
# DOG BONE PART 1 - Draw the circles, in the dog bone
for i in range(0, maxH):
    for j in range(0, maxL):
        if(((circle1.x - i)**2 + (circle1.y - j)**2 ) <= RADIUS**2 ):
            composition[i,j] = DISILICATE
            temperature[i,j] = 1000
        if(((circle2.x - i)**2 + (circle2.y - j)**2 ) <= RADIUS**2 ):
            composition[i,j] = DISILICATE
            temperature[i,j] = 1000

# DOG BONE PART 2 - Draw the "body"
for i in range(0, maxH):
    for j in range(0, maxL):
        # Fill the gap between the circle's center
        # It is splitted with 2 IFs to an easy compreension
        if(circle1.x - LENGTH <= i and i <= circle1.x + LENGTH):
            if (circle1.y <= j and j <= circle2.y):
                composition[i,j] = DISILICATE
                temperature[i,j] = 50

# PLATINUM ELECTRODE
for i in range(0, maxH):
    for j in range(0, maxL):
        if(((circle1.x - i)**2 + (circle1.y - j)**2 ) <= ELECTRODE_RADIUS**2 ):
            composition[i,j] = PLATINUM
            temperature[i,j] = 20
        if(((circle2.x - i)**2 + (circle2.y - j)**2 ) <= ELECTRODE_RADIUS**2 ):
            composition[i,j] = PLATINUM
            temperature[i,j] = 20

# Heat diffusion
print("Start simulation...")
nRun = 0
plt.imshow(temperature, interpolation=INTERPOLATION)
plt.savefig('test'+str(nRun)+'.png', dpi=1000)
while (True):
    nRun += 1
    TOld = temperature
    for i in range(2, maxH-1):
        for j in range(2, maxL-1):
            Tvar = heatDiffusion(TOld[i-1:i+2,j-1:j+2], composition[i-1:i+2,j-1:j+2])
            temperature[i,j] = temperature[i,j] + Tvar
    if (nRun % 10 == 0):
        # Display the image
        print("\nImg exporting ", end='')
        plt.imshow(temperature, interpolation=INTERPOLATION)
        plt.savefig('test'+str(nRun)+'.png', dpi=1000)
        print("-> Img exported")
        #plt.colorbar()
        plt.show()
    else:
        print('.', end='')
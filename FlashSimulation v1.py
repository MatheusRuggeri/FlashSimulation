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

# Obj to help with radius calculation
class circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        if(((circle2.x - i)**2 + (circle2.y - j)**2 ) <= RADIUS**2 ):
            composition[i,j] = DISILICATE
            
# DOG BONE PART 2 - Draw the "body"
for i in range(0, maxH):
    for j in range(0, maxL):
        # Fill the gap between the circle's center
        # It is splitted with 2 IFs to an easy compreension
        if(circle1.x - LENGTH <= i and i <= circle1.x + LENGTH):
            if (circle1.y <= j and j <= circle2.y):
                composition[i,j] = DISILICATE

# PLATINUM ELECTRODE
for i in range(0, maxH):
    for j in range(0, maxL):
        if(((circle1.x - i)**2 + (circle1.y - j)**2 ) <= ELECTRODE_RADIUS**2 ):
            composition[i,j] = PLATINUM
        if(((circle2.x - i)**2 + (circle2.y - j)**2 ) <= ELECTRODE_RADIUS**2 ):
            composition[i,j] = PLATINUM


# Display the image
plt.imshow(composition, interpolation=INTERPOLATION)
#plt.colorbar()
plt.show()
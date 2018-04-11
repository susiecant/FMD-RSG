#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 03:02:11 2018

@author: benjamin
"""

import numpy as np
import random as random
import matplotlib.pyplot as plt
import time
import pandas as pd
import math

class Haversine:
    '''
    use the haversine class to calculate the distance between
    two lon/lat coordnate pairs.
    output distance available in kilometers, meters, miles, and feet.
    example usage: Haversine([lon1,lat1],[lon2,lat2]).feet
    
    '''
    def __init__(self,coord1,coord2):
        lon1,lat1=coord1
        lon2,lat2=coord2
        
        R=6371000                               # radius of Earth in meters
        phi_1=math.radians(lat1)
        phi_2=math.radians(lat2)

        delta_phi=math.radians(lat2-lat1)
        delta_lambda=math.radians(lon2-lon1)

        a=math.sin(delta_phi/2.0)**2+\
           math.cos(phi_1)*math.cos(phi_2)*\
           math.sin(delta_lambda/2.0)**2
        c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
        
        self.km=self.meters/1000.0              # output distance in kilometers

xcoord = CompleteData['lat']
ycoord = CompleteData['long']
cattle = CompleteData['cattle']
sheep = CompleteData['sr']
vac = CompleteData['vaccine']

#Calculate Haversine distances

dist = np.zeros(shape=(292,292))
        
for i in range(0,291):
    for j in range(0,291):
        dist[i,j] = Haversine((CompleteData['lat'][i],CompleteData['long'][i]),(CompleteData['lat'][j],CompleteData['long'][j])).km

dist = dist/100

#Parameter values
        
psi = 0.00657
nu = 1.99*(10**(-7))
xi = 4.65
zeta = 2.80
chi = 0.403
phi = 0.799
rho = 0.000863
epsilon = 0.02 #Vaccine parameter
s = np.random.negative_binomial(50, 50/55, 292) #Draw latent periods
r = np.random.negative_binomial(30, 30/38, 292) #Draw infectious periods

#Calculate distance kernel
K = psi/(psi**2 + dist**2)   
#K = np.exp(-(np.sqrt(dist/phi))) + rho

#Calculate susceptibility

beta1 = np.zeros(292)
beta1 = nu*(xi*(cattle)**chi + (sheep)**chi)

for i in range(0,291):
    if (CompleteData['vaccine'][i] == 1):
       beta1[i] = epsilon*beta1[i]

#Choose initial cases
       
t = 0
A = np.zeros(shape=(292,5))
output = np.zeros(shape=(292,6))       

initial1 = random.randint(0,291)
initial2 = initial1+1
initial3 = initial2+1
I = np.zeros(292)
I[initial1] = 2
I[initial2] = 2
I[initial3] = 2
A[0, ] = [initial1, 0, s[initial1], r[initial1], vac[initial1]]
A[1, ] = [initial2, 0, s[initial2], r[initial2], vac[initial2]]
A[2, ] = [initial3, 0, s[initial3], r[initial3], vac[initial3]]

start_time = time.time()
while sum(I == 1) + sum(I == 2) > 0:

#Calculate transmission rate

    t = t + 1
    print("Day", t, "Exposed", sum(I == 1), "Infected", sum(I == 2), "Culled", sum(I == 3))

    beta = np.zeros(292)

    for j in range(0,291):
        beta[j] = beta1[j]*(np.sum((zeta*(cattle[I == 2]**chi) + sheep[I == 2]**chi)*K[I == 2, j]))

#Calculate probability of infection
    
    prob_inf = 5*(1 - np.exp(-beta))
    
#Infect if probability is less that a uniform sample

    unif = np.random.uniform(0, 1, 292)

    for i in range(0,291):
        if (unif[i] <= prob_inf[i] and I[i] == 0):
            I[i] =  1
            su = sum(I != 0)
            A[su-1, ] = [i, t, s[i], r[i], vac[i]]
            print("Farm", i, "Day", t)
            
#Update states
        
    inf = A[:,0][A[:,1] + A[:,2] == t] #Move to I state once latent period is over
    I[inf.astype(np.int64)] = 2
    rem = A[:,0][A[:,1] + A[:,2] + A[:,3] == t] #Move to R state once infectious period is over
    I[rem.astype(np.int64)] = 3
    out = sum(output[:,1] != 0)
    plt.scatter(xcoord, ycoord, c = 'gray', alpha = 0.05)
    plt.scatter(output[0:out, 2], output[0:out, 3], c = 'red')
    plt.show()
    
#Store output

    if len(rem) > 0:
        for i in range(0,len(rem)):
            output[out + i,] = [rem[i], t - A[i,2] - A[i,3], xcoord[rem.astype(np.int64)[i]], ycoord[rem.astype(np.int64)[i]], cattle[rem.astype(np.int64)[i]], sheep[rem.astype(np.int64)[i]]]

output = output[0:out,]

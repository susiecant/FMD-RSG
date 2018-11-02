#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 21:55:21 2018

@author: benjamin
"""

import numpy as np
import random as random
import matplotlib.pyplot as plt
import time

#Calculate Euclidean distances

dist = np.zeros(shape=(5378,5378))

for i in range(0,5377):
    for j in range(0,5377):
        dist[i,j] = np.sqrt((xcoord[i] - xcoord[j])**2 + (ycoord[i] - ycoord[j])**2)

#Parameter values
        
psi = 0.00657
nu = 1.99*(10**(-7))
xi = 2.65
zeta = 1.80
chi = 0.403
s = np.random.negative_binomial(50, 50/55, 5378) #Draw latent periods
r = np.random.negative_binomial(30, 30/39, 5378) #Draw infectious periods

t = 0
A = np.zeros(shape=(5378,4))
output = np.zeros(shape=(5378,6))

#Calculate distance kernel
K = psi/(psi**2 + dist**2)   


beta1 = np.zeros(5378)
beta1 = nu*(xi*(cattle)**chi + (sheep)**chi)

#Choose initial case

initial = random.randint(0,5377)
I = np.zeros(5378)
I[initial] = 1
A[0, ] = [initial, 0, s[initial], r[initial]]

start_time = time.time()
while sum(I == 1) + sum(I == 2) > 0:

#Calculate transmission rate

    t = t + 1
    print("Day", t, "Exposed", sum(I == 1), "Infected", sum(I == 2), "Culled", sum(I == 3))

    beta = np.zeros(5378)

    for j in range(0,5377):
        beta[j] = beta1[j]*(np.sum((zeta*(cattle[I == 2]**chi) + sheep[I == 2]**chi)*K[I == 2, j]))       

#Calculate probability of infection
    
    prob_inf = 1 - np.exp(-beta)
    
#Infect if probability is less that a uniform sample

    unif = np.random.uniform(0, 1, 5378)

    for i in range(0,5377):
        if (unif[i] <= prob_inf[i] and I[i] == 0):
            I[i] =  1
            su = sum(I != 0)
            A[su-1, ] = [i, t, s[i], r[i]]
            print("Farm", i, "Day", t)
            
#Update states
        
    inf = A[:,0][A[:,1] + A[:,2] == t] #Move to I state once latent period is over
    I[inf.astype(np.int64)] = 2
    rem = A[:,0][A[:,1] + A[:,2] + A[:,3] == t] #Move to R state once infectious period is over
    I[rem.astype(np.int64)] = 3
    out = sum(output[:,1] != 0)
    
#Store output

    if len(rem) > 0:
        for i in range(0,len(rem)):
            output[out + i,] = [rem[i], t - A[i,2] - A[i,3], xcoord[rem.astype(np.int64)[i]], ycoord[rem.astype(np.int64)[i]], cattle[rem.astype(np.int64)[i]], sheep[rem.astype(np.int64)[i]]]

print("--- %s seconds ---" % (time.time() - start_time))

np.savetxt('dist', dist, delimiter = '')

plt.ion()
plt.scatter(xcoord, ycoord, c = 'gray', alpha = 0.05)
plt.show()
plt.set_offsets(3.1, 5.5, c = 'red')

plt.scatter(3.5, 5.5)
plt.scatter(3.5,5)

plt.scatter(output[1:1495,2], output[1:1495,3])
plt.scatter(xcoord, ycoord)


plt.ion()

fig, ax = plt.subplots()

plot = ax.scatter([], [])
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

while True:
    # get two gaussian random numbers, mean=0, std=1, 2 numbers
    point = np.random.normal(0, 1, 2)
    # get the current points as numpy array with shape  (N, 2)
    array = plot.get_offsets()

    # add the points to the plot
    array = np.append(array, point)
    plot.set_offsets(array)

    # update x and ylim to show all points:
    ax.set_xlim(array[:, 0].min() - 0.5, array[:,0].max() + 0.5)
    ax.set_ylim(array[:, 1].min() - 0.5, array[:, 1].max() + 0.5)
    # update the figure
    fig.canvas.draw()

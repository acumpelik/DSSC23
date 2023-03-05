# -*- coding: utf-8 -*-
'''
Homework 1

How would you propose to generalize “z-scoring” (e.g., sub-
traction of the mean, normalization by the standard deviation) from the 1D case
to the multivariate case, where x belongs to R^D? Generate a synthetic dataset with 10^4
data points drawn from bivariate Gaussian distribution with di↵erent means and
standard deviations for both variables (e.g., x̄ 1 = 10, x̄ 2 = 1, and 1 = 2,
2 = 1), and for three di↵erent correlation coefficients (e.g., ⇢ = 0, 0.5, 0.95).
Does your proposed transformation alter the covariance matrix?

'''

import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10)
# x = np.array((1, 1, 2, 3, 3, 5, 7, 8, 9, 10,
#     10, 11, 11, 13, 13, 15, 16, 17, 18, 18,
#     18, 19, 20, 21, 21, 23, 24, 24, 25, 25,
#     25, 25, 26, 26, 26, 27, 27, 27, 27, 27,
#     29, 30, 30, 31, 33, 34, 34, 34, 35, 36,
#     36, 37, 37, 38, 38, 39, 40, 41, 41, 42,
#     43, 44, 45, 45, 46, 47, 48, 48, 49, 50,
#     51, 52, 53, 54, 55, 55, 56, 57, 58, 60,
#     61, 63, 64, 65, 66, 68, 70, 71, 72, 74,
#     75, 77, 81, 83, 84, 87, 89, 90, 90, 91))
# 
# plt.hist(x, bins=10)

# count,bins = np.histogram(x)
# plt.plot(count, bins)

def gaussian(x, x_bar, std):
    mu = np.mean(x)
    sigma = np.std(x)
    denominator = math.sqrt(2*math.pi*std**2) * math.e
    exponent = -1/2 * ((x-x_bar)**2 / std**2)
    p = 1 / denominator * math.e**exponent
    return p, mu, sigma

p, mu, sigma = gaussian(x, 0, 1)

# plt.hist(p, bins=10)

# verify 
print(abs(mu-np.mean(x)))


plt.plot(x,p)

#%%
mu, sigma = 0,1
s = np.random.normal(mu,sigma, 1000)


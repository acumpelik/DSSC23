#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plot the voltage signal x(t) trace1 from the microelectrode
array and visually examine it. Spikes are very fast downward voltage excursions
(sometimes reaching to ~ -100 μV ), followed by a small overshoot (zoom in to
a few spikes to see how they typically look like).

To get some sense of the signal, plot a probability distribution function (properly
normalized, so that the integral of dxP (x) = 1), of x(t). Estimate the error bars on the PDF
by splitting the data multiple times into halves and compute the SD over PDF
estimates constructed from halves of the data. Is there any obvious feature for
negative voltages in the histogram where you could draw a threshold to recognize
the spikes easily? To identify the spikes, you can set a threshold. Scan a range of
thresholds, from 70 μV and 30 μV ; whenever the signal crosses the threshold
in a downward direction (please pay attention to this definition!), identify a
putative spike, and plot the number of spikes as a function of the threshold. By
examining the trace in detail, can you claim that any specific threshold is a good
choice for spike detection?
"""
# %matplotlib auto

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm
import os
datadir = '/home/acumpeli/Documents/DSSC23'
os.chdir(datadir)

trace1 = np.loadtxt(fname=('./trace1.txt')) # import the data

# %%
# Plot trace 1
plt.figure(figsize=(10,4))
plt.plot(trace1)
plt.title('Voltage trace 1')
plt.show()

# Plot a subset
plt.figure(figsize=(10,4))
plt.plot(trace1[0:80_000])
plt.title('Voltage trace 1, subset')
plt.show()

"""
Plot a pdf
"""

# Bin the data
Vmin = trace1.min()

# Plot a histogram







# print(norm.support())

# plt.plot(len(trace1), norm.pdf(trace1))
plt.figure(figsize=(10,5))
plt.plot(trace1, norm.pdf(trace1))
plt.show()
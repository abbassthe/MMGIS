# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 08:19:39 2023

@author: Admin
"""

import h5py
import numpy as np
import matplotlib.pyplot as plt


h5file = h5py.File('ECOSTRESS_L2_LSTE_29372_034_20230910T205241_0601_01.h5', 'r')

dataset_name = 'SDS/Emis1'

dataset = h5file[dataset_name]

data = dataset[:]

h5file.close()

# Compute the FFT of the data
fft_result = np.fft.fft2(data)

# Plot the 2D magnitude spectrum
plt.figure(figsize=(10, 8))
plt.imshow(np.log(np.abs(fft_result)), extent=(-np.pi, np.pi, -np.pi, np.pi))
plt.colorbar(label='Log Magnitude')
plt.title('2D FFT Magnitude Spectrum')
plt.xlabel('Frequency (radians)')
plt.ylabel('Frequency (radians)')
plt.show()
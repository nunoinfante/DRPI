import numpy as np
import matplotlib.pyplot as plt
from imageio.v2 import imread, imwrite


# =============================================================================
# a1 = np.uint8(100)
# a2 = np.uint8(255)
# a3 = np.uint8(105)
# a4 = float(a1)
# a5 = int(a1)
# 
# z1 = a1+a2
# z2 = a1-a3
# z3 = a4-a3
# z4 = np.uint8(z3)
# z5 = np.uint8(a4)
# z6 = a5+a2
# 
# b1 = [[1.2, 2], [3, 4]]
# b2 = [[4, 3.0], [2, 1]]
# b3 = np.uint8(b2)
# 
# c1 = np.array([[1.2, 2], [3, 4]])
# c2 = np.array([[1, 2], [3, 4]])
# c3 = np.uint8(c1)
# 
# c4 = c2.astype(float) 
# c5 = c3.astype(float) 
# c6 = c1.astype(int)
# 
# z7 = b1+b2 
# z8 = b1+b3
# 
# #####################################
# 
# img = imread('einstein01.tif')
# 
# dim = img.shape
# tipo = img.dtype
# npix = img.size
# 
# R = img[:, :, 0].astype(float)
# G = img[:, :, 1].astype(float)
# B = img[:, :, 2].astype(float)
# 
# pond = [0.2989, 0.5870, 0.1140]
# 
# media_pond = pond[0]*R + pond[1]*G + pond[2]*B
# media_arit = (R+G+B)/3
# 
# plt.figure()
# plt.subplot(122);
# plt.imshow(np.uint8(media_pond), 'gray')
# plt.subplot(122);
# plt.imshow(np.uint8(media_arit), 'gray')
# 
# #####################################
# 
# S1 = imread('ferramentas01.tif')
# S2 = imread('ferramentas02.tif')
# 
# Sub1 = np.abs(S2.astype(float) - S1.astype(float))
# Sub2 = (255 - S2.astype(float) + S1.astype(float))/2
#  
# plt.figure()
# plt.imshow(Sub1, 'gray')
# plt.imshow(Sub2, 'gray')
# 
# #####################################
# 
# D1 = imread('texto01.tif')
# D2 = imread('texto02.tif')
# 
# Div = (D1[:, :, 0].astype(float)/D2[:, :, 0].astype(float))
# 
# plt.figure()
# plt.imshow(Div, 'gray')
# 
# #####################################
# 
# S1 = imread('ferramentas01.tif')
# Reg = imread('ferramentas_bin.tif')
# 
# Mult = Reg*S1
# 
# plt.figure()
# plt.imshow(S1, 'gray')
# plt.imshow(Reg, 'gray')
# plt.imshow(Mult, 'gray')
# 
# #####################################
# 
# A = imread('einstein01.tif')
# B = imread('marilyn01.tif')
# 
# dim = A.shape
# k1 = 0.5
# k2 = 0.5
# Ble = np.zeros((dim[0], dim[1], dim[2]))
# 
# for i in range(0, dim[2]):
#     Ble[:, :, i] = k1*A[:, :, i].astype(float) + k2*B[:, :, i].astype(float)
#     
# plt.figure()
# plt.imshow(Ble.astype(np.u))
# 
# #####################################
# 
# B1 = imread('bin01.tif')
# B2 = imread('bin02.tif')
# 
# B = np.logical_and(B1, B2)
# 
# plt.figure()
# plt.imshow(B)
# 
# #####################################
# 
# B1 = imread('bin01.tif')
# B2 = imread('bin02.tif')
# 
# B = np.logical_and(np.logical_not(B1), B2)
# 
# plt.figure()
# plt.imshow(B)
# 
# #####################################?????????????
# 
# B1 = imread('bin01.tif')
# B2 = imread('bin02.tif')
# 
# B = np.logical_xor(B1, B2)
# 
# plt.figure()
# plt.imshow(B)
# =============================================================================

#####################################

B1 = imread('bin01.tif')
B2 = imread('bin02.tif')

B = np.logical_or(np.logical_and(B1, B2), np.logical_or(np.logical_not(B1), np.logical_not(B2)))

plt.figure()
plt.imshow(B)




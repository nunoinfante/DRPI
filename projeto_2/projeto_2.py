# %%
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from imageio.v2 import imread, imwrite

def ELC(img):
    yx = np.column_stack(np.where(img == 255))
    x = np.average([i[1] for i in yx])
    y = np.average([i[0] for i in yx])
    print(yx)

img = imread('Ortokuva.tif')

#exercicio 1
R = img[:, :, 0].astype(float)
G = img[:, :, 1].astype(float)
B = img[:, :, 2].astype(float)

histograma_R, _ = np.histogram(R, bins = 256, range = [0, 256])
histograma_G, _ = np.histogram(G, bins = 256, range = [0, 256])
histograma_B, _ = np.histogram(B, bins = 256, range = [0, 256])

fig, axs = plt.subplots(2, 3)
axs[0, 0].imshow(R, 'gray')
axs[0, 1].imshow(G, 'gray')
axs[0, 2].imshow(B, 'gray')
axs[1, 0].plot(histograma_R, color='red')
axs[1, 0].set_title('R')
axs[1, 1].plot(histograma_G, color='green')
axs[1, 1].set_title('G')
axs[1, 2].plot(histograma_B, color='blue')
axs[1, 2].set_title('B')

fig.tight_layout()

#exercicio 2

histograma, _ = np.histogram(img, bins = 256, range = [0, 256])
fig, axs = plt.subplots(1, 2)
axs[0].imshow(img, 'gray')
axs[1].plot(histograma, color='black')

fig.tight_layout()

#exercicio 3

ELC(img)







# %%

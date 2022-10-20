# %%
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from imageio.v2 import imread, imwrite


img = imread('Ortokuva.tif')

#exercicio 1
R = img[:, :, 0].astype(float)
G = img[:, :, 1].astype(float)
B = img[:, :, 2].astype(float)

histograma_R, _ = np.histogram(R, bins = 256, range = [0, 256])
histograma_G, _ = np.histogram(G, bins = 256, range = [0, 256])
histograma_B, _ = np.histogram(B, bins = 256, range = [0, 256])

# fig, axs = plt.subplots(2, 3)
# axs[0, 0].imshow(R, 'gray')
# axs[0, 1].imshow(G, 'gray')
# axs[0, 2].imshow(B, 'gray')
# axs[1, 0].plot(histograma_R, color='red')
# axs[1, 0].set_title('R')
# axs[1, 1].plot(histograma_G, color='green')
# axs[1, 1].set_title('G')
# axs[1, 2].plot(histograma_B, color='blue')
# axs[1, 2].set_title('B')

# fig.tight_layout()

#exercicio 2
h, _ = np.histogram(img, bins = 256, range = (0, 256))
# fig, axs = plt.subplots(1, 2)
# axs[0].imshow(img, 'gray')
# axs[1].plot(h, color='gray')

# fig.tight_layout()

#exercicio 3
a = np.min(img)
b = np.max(img)
c = 0
d = 255
img_elc = (img-a)*((d-c)/(b-a))+c

h_elc, _ = np.histogram(img_elc, bins = 256, range = (0, 256))

#exercicio 4
saturacao = 10/100
p = h.astype(float)/(np.size(img))
pa = np.cumsum(p)
a1 = float(np.count_nonzero(pa <= saturacao/2) - 1)
b1 = float(np.count_nonzero(pa <= (1-saturacao/2)) - 1)
elc_sat = (img-a1)*((d-c)/(b1-a1))+c

h_elc_sat, _ = np.histogram(elc_sat, bins = 256, range = (0, 256))

#exercicio 6

fig, axs = plt.subplots(2, 3)
axs[0, 0].imshow(img, 'gray')
axs[0, 1].imshow(np.uint8(img_elc), 'gray', vmin=0, vmax=255)
axs[0, 2].imshow(np.uint8(elc_sat), 'gray', vmin=0, vmax=255)
axs[1, 0].plot(h)
axs[1, 1].plot(np.uint8(h_elc))
axs[1, 2].plot(np.uint8(h_elc_sat))



# %%

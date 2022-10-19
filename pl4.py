import matplotlib.pyplot as plt
import numpy as np
from imageio.v2 import imread

A = imread('sat.tif').astype(float)

h, _ = np.histogram(A, bins=256, range=(0, 256))

#1.1
a = np.min(A)
b = np.max(A)
c = 0
d = 255

elc = (A-a)*((d-c)/(b-a))+c
h_elc, _ = np.histogram(np.uint8(elc), bins=256, range=(0, 256))

#1.2
saturacao = 30/100
p = h.astype(float)/(np.size(A))
pa = np.cumsum(p)
a1 = float(np.count_nonzero(pa <= saturacao/2) - 1)
b1 = float(np.count_nonzero(pa <= (1-saturacao/2)) - 1)

elc_sat = (A-a1)*((d-c)/(b1-a1))+c
h_elc_sat, _ = np.histogram(np.uint8(elc_sat), bins=256, range=(0, 256))


#2.1
ha = np.cumsum(h)
p = h/float(np.size(A))
pa = np.cumsum(p)
pa_norm = pa*(256-1)
eq = np.zeros(A.shape)
for i in range(len(pa_norm)):
    eq = eq+(A==i)*int(pa_norm[i])

heq, _ = np.histogram(np.uint8(eq), bins=256, range=(0, 256))

# plt.figure()
# plt.subplot(231)
# plt.imshow(A, 'gray', vmin=0, vmax=255)
# plt.subplot(232)
# plt.imshow(np.uint8(eq), 'gray', vmin=0, vmax=255)
# plt.subplot(233)
# plt.plot(h)
# plt.subplot(234)
# plt.plot(ha)
# plt.subplot(235)
# plt.plot(heq)
# plt.subplot(111)
# plt.plot(np.cumsum(eq))

# plt.tight_layout()

#3

B = imread('iceberg.tif').astype(float)

const = 255/np.log10(1+np.max(np.abs(B)))
Log = const*np.log10(1+np.abs(B))

base = 1.01
Exp = base**B
elc_exp = (Exp-np.min(Exp))*((d-c)/(np.max(Exp)-np.min(Exp)))+c


pot = 0.5
outPot = B**pot
elc_pot = (outPot-np.min(outPot))*((d-c)/(np.max(outPot)-np.min(outPot)))+c

plt.figure
plt.subplot(221)
plt.imshow(np.uint8(B), 'gray')
plt.subplot(222)
plt.imshow(np.uint8(elc_pot), 'gray', vmin=0, vmax=255)





























from imageio.v2 import imread, imwrite
import matplotlib.pyplot as plt
import numpy as np
import math

img = imread("marilyn.tif")

ang = np.radians(-45) 
dx = 0
dy = 0
sx = 1
sy = 1

a1 = sx*math.cos(ang)
b1 = sx*math.sin(ang)
c1 = sy*(-math.sin(ang))
d1 = sy*math.cos(ang)
e1 = dx
f1 = dy

mat = np.array([[a1, c1, e1],
                [b1, d1, f1],
                [0, 0, 1]])

col0 = img.shape[1]
lin0 = img.shape[0]

xx = np.linspace(0, col0-1, col0)
yy = np.linspace(0, lin0-1, lin0)
x0 = np.reshape(np.meshgrid(xx, yy)[0], lin0*col0)
y0 = np.reshape(np.meshgrid(xx, yy)[1], lin0*col0)

xyz = np.ones((3, len(x0)))
xyz[0, :] = x0
xyz[1, :] = y0
xyz1 = np.matmul(mat, xyz)

x1 = xyz1[0, :]+e1
y1 = xyz1[1, :]+f1

outxy = np.where((x1 < 0) | (x1 >= col0) | (y1 < 0) | (y1 >= lin0))
x1[outxy] = 0
y1[outxy] = 0

xpix = x1.astype(int)
ypix = y1.astype(int)
out_directa = np.zeros((lin0, col0))
out_directa[ypix, xpix] = img[y0.astype(int), x0.astype(int)]




from skimage.transform import rotate

Rot = rotate (img, ang, resize=False, order=1)
plt.figure()
plt.subplot(121)
plt.imshow(np.uint8(img), 'gray')
plt.subplot(122)
plt.imshow(Rot, 'gray')























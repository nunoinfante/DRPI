# Projeto 1
# Nuno Infante 55411


import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from imageio.v2 import imread, imwrite

img1 = imread('Mars_Reconnaissance_11.tif')
img2 = imread('Mars_Reconnaissance_22.tif')

plt.figure()
plt.subplot(141)
plt.imshow(img1, 'gray')
plt.subplot(142)
plt.imshow(img2, 'gray')

# exercício 1
Sub1 = np.abs(img1.astype(float) - img2.astype(float))
Sub1[Sub1 < 100] = 0
Sub1[Sub1 > 100] = 255

plt.subplot(143)
plt.imshow(Sub1, 'gray')

#exercicio 2
def coords_marcadores(img):
    modulo = img[0:200]
    paraquedas = img[600:700]
    
    coords_modulo = np.column_stack(np.where(modulo == 255))
    coords_paraquedas = np.column_stack(np.where(paraquedas == 255))
    y_paraquedas = np.average([i[0]+600 for i in coords_paraquedas])
    x_paraquedas = np.average([i[1] for i in coords_paraquedas])
    y_modulo = np.average([i[0] for i in coords_modulo])
    x_modulo = np.average([i[1] for i in coords_modulo])
    return [[y_modulo, x_modulo], [y_paraquedas, x_paraquedas]]

#retorna o número de pixels da escala
def nrPixelEscala(img):
    imgEscala = img[47:70]
    yx_escala = np.column_stack(np.where(imgEscala == 0))
    x_escala = [i[1] for i in yx_escala]
    return max(x_escala) - min(x_escala) + 1

escala = nrPixelEscala(img2) # o valor de escala equivale a 200 metros
coordenadas = coords_marcadores(Sub1)
distancia_pixel = math.dist(coordenadas[0], coordenadas[1])
distancia_aproximada = (distancia_pixel*200)/escala
print(f'Distancia aproximada: {distancia_aproximada} metros')

# exercicio 3
ee = ndimage.generate_binary_structure(2,2)
L, n = ndimage.label(Sub1, ee)
cm = ndimage.center_of_mass(Sub1, L, [1, 2])
dist_cm = math.dist(cm[0], cm[1])

dpi = 72
distancia_impressa = dist_cm/dpi*0.025400051
escala_impressa = nrPixelEscala(img2)/dpi*0.025400051 # o valor equivale a 200 metros
distancia_real = (200*distancia_impressa)/escala_impressa
print(f'Distancia real: {distancia_real} metros')

# exercicio 4
x = [cm[0][1], cm[1][1]]
y = [cm[0][0], cm[1][0]]

plt.subplot(144)
plt.plot(x, y, color='blue', linewidth=0.5)
plt.text(15, 700, f'Distância = {int(np.round(distancia_real))} m', color='blue', fontsize=7.4)
plt.imshow(img2,'gray')
plt.tight_layout()
plt.show()
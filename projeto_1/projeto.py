# Projeto 1
# Nuno Infante 55411


import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from imageio.v2 import imread, imwrite

#Ler imagens
img1 = imread('Mars_Reconnaissance_11.tif')
img2 = imread('Mars_Reconnaissance_22.tif')

#Mostrar imagens
plt.figure()
plt.subplot(141)
plt.imshow(img1, 'gray')
plt.subplot(142)
plt.imshow(img2, 'gray')

# exercício 1

#Subtração das duas imagens originais
Sub1 = np.abs(img1.astype(float) - img2.astype(float))

#Para cada pixel, se tiver menos de 100 atribui o valor 0, se tiver mais que 100 atribui o valor 255
Sub1[Sub1 < 100] = 0
Sub1[Sub1 > 100] = 255

#Mostra a imagem binária
plt.subplot(143)
plt.imshow(Sub1, 'gray')

#exercicio 2

#Retorna as coordenadas dos marcadores
def coords_marcadores(img):

    #Corta a imagem em duas, uma com o modulo e outra com o paraquedas
    modulo = img[0:200]
    paraquedas = img[600:700]
    
    coords_modulo = np.column_stack(np.where(modulo == 255)) #Coordenadas de cada pixel do módulo com o valor 255
    coords_paraquedas = np.column_stack(np.where(paraquedas == 255)) #Coordenadas de cada pixel do paraquedas com o valor 255
    y_paraquedas = np.average([i[0]+600 for i in coords_paraquedas]) #Média das coordenadas y do paraquedas
    x_paraquedas = np.average([i[1] for i in coords_paraquedas]) #Média das coordenadas x do paraquedas
    y_modulo = np.average([i[0] for i in coords_modulo]) #Média das coordenadas y do modulo
    x_modulo = np.average([i[1] for i in coords_modulo]) #Média das coordenadas x do modulo
    return [[y_modulo, x_modulo], [y_paraquedas, x_paraquedas]] 

#Retorna o numero de pixels da escala
def nrPixelEscala(img):
    imgEscala = img[47:70] #Corta a imagem com a escala
    yx_escala = np.column_stack(np.where(imgEscala == 0)) #Coordenadas de cada pixel da escala com o valor 0
    x_escala = [i[1] for i in yx_escala] #Lista com as coordenadas x de todas as coordenadas da escala
    return max(x_escala) - min(x_escala) + 1

escala = nrPixelEscala(img2) # o valor de escala equivale a 200 metros
coordenadas = coords_marcadores(Sub1) # coordenadas dos marcadores
distancia_pixel = math.dist(coordenadas[0], coordenadas[1]) # distancia entre o modulo e o paraquedas
distancia_aproximada = (distancia_pixel*200)/escala # distancia aproximada em metros usando a escala
print(f'Distancia aproximada: {distancia_aproximada} metros')

# exercicio 3
ee = ndimage.generate_binary_structure(2,2)
L, n = ndimage.label(Sub1, ee)
cm = ndimage.center_of_mass(Sub1, L, [1, 2])

dist_cm = math.dist(cm[0], cm[1]) # distancia entre o modulo e o paraquedas

dpi = 72 # dpi retirado dos metadados da imagem
distancia_impressa= dist_cm/dpi*0.025400051 # distancia impressa em metros entre o modulo e paraquedas
escala_impressa = nrPixelEscala(img2)/dpi*0.025400051 # o valor equivale a 200 metros
distancia_real = (200*distancia_impressa)/escala_impressa # distancia em metros entre o modulo e paraquedas
print(f'Distancia real: {distancia_real} metros')

# exercicio 4

x = [cm[0][1], cm[1][1]] # coordenada x do modulo e paraquedas
y = [cm[0][0], cm[1][0]] # coordenada y do modulo e paraquedas

# mostra a imagem com a linha entre o modulo e paraquedas
plt.subplot(144)
plt.plot(x, y, color='blue', linewidth=0.5)
plt.text(15, 700, f'Distância = {int(np.round(distancia_real))} m', color='blue', fontsize=7.4)
plt.imshow(img2,'gray')
plt.tight_layout()
plt.show()
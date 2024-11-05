import cv2
import pywt
import matplotlib.pyplot as plt

#Carregar uma imagem
imagem = cv2.imread('moto2.webp', cv2.IMREAD_GRAYSCALE)

#Realizar decomposição da imagem em Wavelets
coeffs2 = pywt.dwt2(imagem, 'haar')

#Usando Wavelets 'haar'
# LL = aproximações
# LH, HL, HH = detalhes
LL, (LH, HL, HH) = coeffs2 

#Mostrar resultados
plt.figure(figsize=(5, 5))

#Imagem Original
plt.subplot(1, 2, 1)
plt.imshow(imagem, cmap= 'gray')
plt.title('Imagem Original')
plt.axis('off')

#LL (Aproximações)
plt.subplot(1, 2, 2)
plt.imshow(LL, cmap='gray')
plt.title('Aproximações')
plt.axis('off')

plt.tight_layout()
plt.show()
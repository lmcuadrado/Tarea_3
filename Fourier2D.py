import numpy as np
import matplotlib.pylab as plt
from scipy import misc

#---------------- Punto 4.1 -----------------#
image=plt.imread('arbol.png')

#---------------- Punto 4.2 -----------------#
img_ft = np.fft.fft2(image)
img_freq=np.fft.fftshift(img_ft)
rango=30*np.log(np.abs(img_freq))

plt.figure()
plt.imshow(rango)
plt.savefig("CuadradoLiliana_FT2D.pdf")

#---------------- Punto 4.2 -----------------#

def filtro(freq, ft):
	for i in range(np.shape(freq)[0]):
		for j in range(np.shape(freq)[0]):
			if(abs(ft[i,j])>2000.0 and abs(ft[i,j]<5000.0)):
				ft[i,j]=0.0
	return ft

#plt.figure()
#plt.plot(img_freq, filtro(img_freq, img_ft))
#plt.show()

#---------------- Punto 4.4 -----------------#
img_ftinversa = np.fft.ifft2(image)		#inversa
img_freq2=np.fft.fftshift(img_ftinversa)
rango2=30*np.log(np.abs(img_freq2))

plt.figure()
plt.imshow(rango2)
plt.savefig("CuadradoLiliana_Imagen_filtrada.pdf")

















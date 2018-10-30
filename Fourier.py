import numpy as np
import matplotlib.pylab as plt

#--------------------- Punto 3.1----------------------------#
signal=np.genfromtxt("signal.dat",delimiter=",")
incompletos=np.genfromtxt("incompletos.dat",delimiter=",")

#--------------------- Punto 3.2----------------------------#
x=signal[1:,0]
y=signal[1:,1]
#print y

plt.figure()
plt.plot(x,y)
plt.title("Grafica de signal")
plt.savefig("CuadradoLiliana_signal.pdf")

#--------------------- Punto 3.3----------------------------#

N=len(y) 
dt=y[2]-y[1]
transformada=np.array([])

#Implementacion de la transformada de fourier
for n in range(1,N+1):
	for k in range(0,N-1):	
		G=np.sum(y[k]*np.exp(-1j*2*np.pi*k*(float(n)/N)))
		transformada=np.append(transformada, G)
print len(transformada)
	


#Lo siguiente es para verificar que su codigo este bien:
from scipy.fftpack import fft, fftfreq
fft_x = fft(y) / N # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias
print len(fft_x)


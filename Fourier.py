import numpy as np
import matplotlib.pylab as plt
import scipy
from scipy import interpolate

#--------------------- Punto 3.1 ----------------------------#
signal=np.genfromtxt("signal.dat",delimiter=",")
incompletos=np.genfromtxt("incompletos.dat",delimiter=",")

#--------------------- Punto 3.2 ----------------------------#
x=signal[:,0]
y=signal[:,1]

x1=incompletos[:,0]
y1=incompletos[:,1]

plt.figure()
plt.plot(x,y)
plt.title("Grafica de signal")
plt.savefig("CuadradoLiliana_signal.pdf")

#--------------------- Punto 3.3 ----------------------------#
N=len(y) 
dt=y[2]-y[1]

#Implementacion de la transformada de fourier

G=np.zeros((N,1), dtype=complex)
for n in range(1,N+1):
	for k in range(0,N-1):	
		G[k]=np.sum(y[k]*np.exp(-1j*2*np.pi*k*(float(n))/N))


#--------------------- Punto 3.4 ----------------------------#

from scipy.fftpack import fft, fftfreq
fft_x = fft(y)/N  # FFT 
freq = fftfreq(N, dt) # Recuperamos las frecuencias

plt.figure()
plt.plot(freq, abs(fft_x))
plt.savefig("CuadradoLiliana_TF.pdf")

#--------------------- Punto 3.5 ----------------------------#

print "Analizando la grafica nos dan 0.014112 y 0.038141"

#--------------------- Punto 3.6 ----------------------------#

fc=1000 
inverse=np.fft.ifft(y)

def pasabajas(freq,fft_x,fc):
	filtro=fft_x
	for i in range(0,len(freq)):
		if freq[i]>fc:
			filtro[i].append(0)
	return filtro
			
filtro=pasabajas(freq,inverse,fc)

plt.figure()
plt.plot(filtro)
plt.savefig("CuadradoLiliana_filtrada.pdf")


#--------------------- Punto 3.7 ----------------------------#

print "No se puede hacer la transformada de fourier en incompletos porque el numero de datos debe ser una potencia de dos. Incompletos tiene una longitud de 117, por eso interpolaremos los datos 512"

#--------------------- Punto 3.8 ----------------------------#
puntos=np.linspace(min(x1),max(x1),512)
quadratic=interpolate.interp1d(x1,y1,kind='quadratic')
cubic=interpolate.interp1d(x1,y1,kind='cubic')

fft_quadratic = fft(quadratic(puntos))/len(puntos)
fft_cubic = fft(cubic(puntos))/len(puntos)

#--------------------- Punto 3.9 ----------------------------#
plt.figure()

plt.subplot(2,2,1)
plt.plot(freq, abs(fft_x))
plt.title("signal")

plt.subplot(2,2,2)
plt.plot(freq, abs(fft_cubic))
plt.title("cubic")

plt.subplot(2,2,3)
plt.plot(freq, abs(fft_quadratic))
plt.title("quadratic")
plt.savefig("CuadradoLiliana_TF_interpola.pdf")

#--------------------- Punto 3.10 ----------------------------#

print "Las graficas de interpolaciones tienen mas ruido "

#--------------------- Punto 3.11 ----------------------------#
 
fc1=500

fc1_signal= pasabajas(freq,fft_x,fc1) #pasabajas aplicado a signal con frecuencia de corte igual a 500

fc1_quadratic= pasabajas(freq,fft_quadratic,fc1) #pasabajas aplicado a quadratic con frecuencia de corte igual a 500
fc_quadratic= pasabajas(freq,fft_quadratic,fc) #pasabajas aplicado a signal con frecuencia de corte igual a 1000

fc1_cubic= pasabajas(freq,fft_cubic,fc1) #pasabajas aplicado a cubic con frecuencia de corte igual a 500
fc_cubic= pasabajas(freq,fft_cubic,fc) #pasabajas aplicado a cubic con frecuencia de corte igual a 1000

#--------------------- Punto 3.12 ----------------------------#

plt.figure(figsize=(12,8))

plt.subplot(3,2,1)
plt.plot(fc1_signal)
plt.title("signal_fc=500")

plt.subplot(3,2,2)
plt.plot(filtro)
plt.title("signal_fc=1000")

plt.subplot(3,2,3)
plt.plot(fc1_quadratic)
plt.title("quadratic_fc=500")

plt.subplot(3,2,4)
plt.plot(fc_quadratic)
plt.title("quadratic_fc=1000")

plt.subplot(3,2,5)
plt.plot(fc1_cubic)
plt.title("cubic_fc=500")

plt.subplot(3,2,6)
plt.plot(fc_cubic)
plt.title("cubic_fc=1000")

plt.subplots_adjust(hspace=.5) 


plt.savefig("CuadradoLiliana_2Filtros.pdf")


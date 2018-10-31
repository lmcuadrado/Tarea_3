import numpy as np
import matplotlib.pylab as plt

#--------------------- Punto 3.1 ----------------------------#
signal=np.genfromtxt("signal.dat",delimiter=",")
incompletos=np.genfromtxt("incompletos.dat",delimiter=",")

#--------------------- Punto 3.2 ----------------------------#
x=signal[:,0]
y=signal[:,1]
#print y

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

print len(G)


#--------------------- Punto 3.4 ----------------------------#

from scipy.fftpack import fft, fftfreq
fft_x = fft(y)/N  # FFT Normalized
freq = fftfreq(N, dt) # Recuperamos las frecuencias

plt.figure()
plt.plot(freq, abs(fft_x))
plt.savefig("CuadradoLiliana_TF.pdf")

#--------------------- Punto 3.5 ----------------------------#

print "Analizando la grafica nos dan 0.014112 y 0.038141"

#--------------------- Punto 3.6 ----------------------------#

fc=1000
#fft_x[abs(freq) < fc] = 0

def pasabajas(freq):
	#filtro=[]
	for i in range(0,len(freq)):
		if freq[i]>fc:
			fft_x[i]=0
	return fft_x
			
filtro=pasabajas(freq)

plt.figure()
plt.plot(filtro)
plt.savefig("CuadradoLiliana_filtrada.pdf")
#plt.show()














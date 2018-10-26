import numpy as np
#import matplotlib.pylab as plt

#Almaceno los datos
datos = (np.genfromtxt("WDBC.dat",delimiter=","))[:,2:] #Selecciono todas las filas y a partir de la segunda columna

def MatCovarianza(a):
	covarianza=np.zeros((np.shape(a)[1],np.shape(a)[1]))	
	for i in range(np.shape(a)[1]):
		for j in range(np.shape(a)[1]):			
			b= a[:,i]-np.mean(a[:,i])
			c= a[:,j]-np.mean(a[:,j])
			bc=b*c
			suma=np.sum(bc)/(np.shape(a)[0]-1)
			covarianza[i,j]=suma
	return covarianza

cov=MatCovarianza(datos)
autovainas=np.linalg.eig(cov)
eigvals=((autovainas)[:1])[0] 
eigvec=((autovainas)[:2])[1]

print eigvals
#for i in range(len(eigvals)):
#	print "autovector",i+1,":", eigvec[i], "autovalor",i+1,":", eigvals[i]


import numpy as np
import heapq
import matplotlib.pylab as plt

#------------ Punto 2.1 --------------#
#Almaceno los datos
datos = (np.genfromtxt("WDBC.dat",delimiter=","))[:,1:]

daticos= (np.genfromtxt("WDBC.dat",delimiter=",", dtype=str))[:,1]

for i in range(len(daticos)):
	if daticos[i]=="M":
		daticos[i]=1.	#El valor 1 corresponde a tumores malignos
	else:	
		daticos[i]=0.	#El valor 0 corresponde a tumores benignos

datos[:,0]=daticos
#print datos

#----------- Punto 2.2 -------------#
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
eigval,eigvec=np.linalg.eig(cov)

print cov

#------------ Punto 2.3 --------------#
for i in range(len(eigval)):
	print "autovector",i+1,":", eigvec[:,i], "autovalor",i+1,":", eigval[i]


#------------ Punto 2.4 --------------#

vec1,vec2=(eigvec[:,0],eigvec[:,1]) #Los dos primeros autovalores son los dos mas grandes y estan asociados con los dos primeros vectores

def porcentajes(vec1):			
	sumita=np.sum(vec1)
	porcentaje=np.zeros(len(vec1))
	for i in range(len(vec2)):
		perce=(vec1[i]*100)/sumita
		porcentaje[i]=perce
	return porcentaje

max_parame1=heapq.nlargest(4,xrange(len(porcentajes(vec1))), key=porcentajes(vec1).__getitem__)
max_parame2=heapq.nlargest(4,xrange(len(porcentajes(vec2))), key=porcentajes(vec2).__getitem__)

maximos=np.array([])
for i in max_parame1:
	for j in max_parame2:
		if i==j:
			maximos=np.append(maximos,i)

print "los parametros mas importantes en base a los autovector son los correspondientes a las columnas:", maximos[0], "y", maximos[1]
	
#------------ Punto 2.5 --------------#
vectores=np.array([vec1,vec2])

proyeccion=np.dot(vectores, np.transpose(datos))
PC1=proyeccion[0,:]
PC2=proyeccion[1,:]

x_verdes=[]
y_verdes=[]
x_rojos=[]
y_rojos=[]

for i in range(len(daticos)):
	if daticos[i]=="0.0":
		x_verdes.append(PC1[i])
		y_verdes.append(PC2[i])
	else:
		x_rojos.append(PC1[i])
		y_rojos.append(PC2[i])
		

plt.figure()
plt.scatter(x_verdes,y_verdes, color="green", label="Benigno")
plt.scatter(x_rojos,y_rojos, color="red", label="Maligno")
plt.legend()
plt.savefig("CuadradoLiliana_PCA.pdf")
















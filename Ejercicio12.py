#! /usr/bin/env python3

#import math para poder escribir el seno
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

#La función de la matriz es que la primera columna representa los gammas, la segunda B, la tercera w_0 y la cuarta w
A=[[0.1,0,2,3],[0,0,2,3],[1,2,1,4],[1,2,4,1],[0.1,0,1,1],[0.1,2,1,1]]
for i in range(len(A)):
	def dU_dx_i(U, x):
		gamma = A[i][0] #Constante de amortiguamiento
		B = A[i][1] #Fuerza externa
		w_0 = A[i][2] #Frecuencia natural del oscilador
		w = A[i][3] #Periodo de frecuencia de la fuerza externa
	#U es un vector tal que U[0]=y e z=U[1]
	#Lo que sigue retorna [y',z'], osea y'=z e z'=-gamma*y'-w_0²*y+B*sin(w*x)
		return [U[1], -gamma*U[1]-w_0*w_0*U[0]+B*math.sin(w*x) ]
#El siguiente comando no es del todo requerido pero hace que se amplie la vista
fig = plt.figure(figsize=(12,7))
#Este siguiente comando es estético, hspace "separa" los gráficos
plt.subplots_adjust(hspace = 0.5, bottom = 0, wspace=0.5)
#Lo siguiente es para dar un título principal
plt.suptitle('Oscilaciones forzadas amortiguadas con una inhomogeneidad')
#Condiciones iniciales, y(0)=1 e y'(0)=0
U0 = [1,0]
#Rango de x de [0,100], 500 son lo nsamplings
xs = np.linspace(0,100,500)
for i in range(len(A)):
	Us = odeint(dU_dx_i, U0, xs)
	ys = Us[:,0]
	#el plt.subplot(3,3,i+1) es para que me aparezcan los gráficos en 3 filas y 3 columnas, 
	#el i+1 es para acomodarlas (notar que i empiza en 0, se le suma uno para que sea desde 1), con esto
	#me refiero a que la primer gráfica irá en la fila 1 columna 1, la segunda en fila 1 columna 2, y así...
	ax = plt.subplot(3,3,i+1)
	ax.plot(xs,ys)
	#Ponemos etiquetas a los ejes
	ax.set_xlabel("Eje x")
	ax.set_ylabel("Eje y")
	#Ponemos un título, los str son necesarios para que los reemplace por los valores adecuados
	ax.set_title('$\gamma $= '+str(A[i][0])+', B = '+str(A[i][1])+', $w_0$ = '+str(A[i][2])+', w = '+str(A[i][3]))
#Para que me lo muestre todo
fig.savefig('Ejercicio12')
plt.show()

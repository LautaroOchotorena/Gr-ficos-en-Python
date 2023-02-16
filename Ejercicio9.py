#! /usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#lee los datos del archivo datos.dat (yo hice un ejemplo con pocos puntos pero se podría extender)
x, y = np.loadtxt("datos.dat",usecols=(0,1), unpack=True)

#La regresión lineal
gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y)

#Veo el mínimo y máximo de x
min_x=np.min(x)
max_x=np.max(x)

#Genera la recta fiteada
x_fit=np.linspace(min_x,max_x,500)
y_fit=gradient*x_fit+intercept

plt.plot(x,y, 'x',label='Datos')
plt.plot(x_fit,y_fit,label='Fiteo lineal')

plt.xlabel('X')
plt.ylabel('Y')

#Armo la recta,.4f indica que va a considerar 4 decimales
recta_lable = "y= %.4f x + (%.4f)" % (gradient, intercept)

#Para que aparezca la ecuación de la recta uso lo siguiente. Ojo: el xy=(0,1) este punto tiene que 
#poderse ver en el gráfico (no me refiero a la recta) para que me muestre la 
#ecuación de la recta, esto se utiliza para decir por ejemplo dónde hay un máximo, un mínimo, etc.
plt.annotate(recta_lable, xy=(0, 1), xycoords='data', 
             xytext=(0.2, 0.95), textcoords='axes fraction', 
             horizontalalignment='left', verticalalignment='top', 
             )

#Nombre del gráfico
plt.title('Ajuste lineal por cuadrados mínimos')

#Guardar como...
plt.savefig('Ejerciicio 9 - Ajuste_lineal.png')

plt.show()

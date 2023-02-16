#! /usr/bin/env python3

#import math para poder escribir e^(-y)
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def dy_dx(y, x):
	return x*math.exp(-y)

xs = np.linspace(0,100,500)
y0 = 1.0 #Condición inicial
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()

#Nombre del gráfico
plt.title('Solución al problema de valores inciales')

#Graficamos la solución
plt.rcParams.update({'font.size': 14})
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.plot(xs, ys)
plt.savefig('Ejercicio11')
plt.show()

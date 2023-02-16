#! /usr/bin/env python3
import math
import numpy as np
import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
#Defino la función
def z(x,y):
  return x**2-y**2

fig = pl.figure()
fig.suptitle('$z=x^2-y^2$')
#Datos del  primer gráfico
ax = fig.add_subplot(2, 1, 1, projection='3d')
x = np.linspace(-5,5,50)
y = np.linspace(-5,5,50)
x, y = np.meshgrid(x, y)
ax.plot_surface(x, y, z(x,y), rstride=1, cstride=1, cmap=pl.cm.hot)
ax.set_zlim(-25,25)


#Ahora veré las curvas de nivel
ax = fig.add_subplot(2, 1, 2)
ax.contourf(x, y, z(x,y), 8, alpha=.75, cmap=pl.cm.hot)
Numcurvas = 6
#Las curvas de nivel aparecerán en negro
C = ax.contour(x, y, z(x,y), Numcurvas, colors='black')
ax.clabel(C, inline=1, fontsize=10)

fig.savefig('Ejercicio8')
pl.show()
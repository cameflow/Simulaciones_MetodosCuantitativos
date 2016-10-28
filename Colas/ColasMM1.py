##################################
##            M/M/1             ##
##################################

from math import *

l = 3 #Tiempo de llegada
miu = 4 #Tiempo de servicio
k = 2 #Cantidad de gente en el sistema (Para la probabilidad de que haya mayor que k)
m = 2 #Cantidad de Servidores
miu *= m

L = l/(miu-l)
Lq = (l*l)/(miu*(miu-l))
W = 1/(miu-l)
Wq = l/(miu*(miu-l))
ro = l/miu
P0 = 1-ro
Pk = (l/miu)**(k+1)

print ("M/M/1")
print ("L (Gente en el sistema):",L)
print ("Lq (Gente en cola):",Lq)
print ("W (Tiempo en el sistema):",round(W,3))
print ("Wq (Tiempo en Fila):",round(Wq,3))
print ("Ro (Rate of use):",round(ro,3))
print ("P0 (Probabilidad sistema vacío):",round(P0,3))
print ("Pk (Probabilidad de mayor de",k,"):", round(Pk,4))
print()

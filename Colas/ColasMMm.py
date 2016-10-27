##################################
##            M/M/M             ##
##################################
from math import *

l = 4 #Llegadas por periodo de tiempo
miu = 5 #Cuantos se atienden en el periodo
m = 2 #Cantidad de servidores
k = 4 #Cantidad de gente en el sistema (Para la probabilidad de que haya mayor que k)
Cs = 8 #Costo por servicio
Cw = 10 #Costo por espera

cont = 0
P0 = 0
while (cont <= m-1):
    P0 += (1/factorial(cont))*((l/miu)**cont)
    cont += 1
P0 += (1/factorial(m))*((l/miu)**m)*((m*miu)/((m*miu)-l))
P0 = 1/P0

L = round((((l*miu*(l/miu)**m)/(factorial(m-1)*(m*miu-l)**2))*P0) + (l/miu),3)

W = L/l
Lq = L - (l/miu)
Wq = W - (1/miu)
ro = l/(m*miu)
Pk = (l/miu)**(k+1)

CT = (m*Cs) + (l*W*Cw)

print ("M/M/m")
print ("Con", m, "servidores")
print ("L (Gente en el sistema):",round(L,5))
print ("Lq (Gente en cola):",round(Lq,5))
print ("W (Tiempo en el sistema):",round(W,5))
print ("Wq (Tiempo en Fila):",round(Wq,5))
print ("Ro (Rate of use):",round(ro,5))
print ("P0 (Probabilidad sistema vacío):",round(P0,5))
print ("Pk (Probabilidad de mayor de k):", round(Pk,4))
print ("CT:",round(CT,5))
print()

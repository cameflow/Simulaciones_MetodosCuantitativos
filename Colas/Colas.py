# Sistema M/M/1
from math import *
from decimal import *

l = 210
miu = 280
k = 4

L = l/(miu-l)
Lq = (l*l)/(miu*(miu-l))
W = 1/(miu-l)
Wq = l/(miu*(miu-l))
ro = l/miu
P0 = 1-ro
Pk = (l/miu)**(k+1)

print ("M/M/1")
print ("L:",L)
print ("Lq:",Lq)
print ("W:",round(W,3))
print ("Wq:",round(Wq,3))
print ("Ro:",round(ro,3))
print ("P0:",round(P0,3))
print ("Pk", round(Pk,4))
print()

#--------------------------------------------------------------------------------------------#
#
# r = 1
# x = 1
# cantidadServ = 0
# CTmenor = 10000000
# while (r <= x):
#     # Sistema M/M/m
#     l = 37.5 #Llegadas por periodo de tiempo
#     miu = 6 #Cuantos se atienden en el periodo
#     m = r #Cantidad de servidores
#     Cs = 8 #Costo por servicio
#     Cw = 10 #Costo por espera
#
#     cont = 0
#     P0 = 0
#     while (cont <= m-1):
#         P0 += (1/factorial(cont))*((l/miu)**cont)
#         cont += 1
#     P0 += (1/factorial(m))*((l/miu)**m)*((m*miu)/((m*miu)-l))
#     P0 = 1/P0
#
#     L = round((((l*miu*(l/miu)**m)/(factorial(m-1)*(m*miu-l)**2))*P0) + (l/miu),3)
#
#     W = L/l
#     Lq = L - (l/miu)
#     Wq = W - (1/miu)
#     ro = l/(m*miu)
#
#     CT = (m*Cs) + (l*W*Cw)
#     if (CT < CTmenor):
#         CTmenor = CT
#         cantidadServ = r
#
#     print ("M/M/m")
#     print ("Con", m, "servidores")
#     print ("L:",round(L,5))
#     print ("Lq:",round(Lq,5))
#     print ("W:",round(W,5))
#     print ("Wq:",round(Wq,5))
#     print ("Ro:",round(ro,5))
#     print ("P0:",round(P0,5))
#     print ("CT:",round(CT,5))
#     print()
#     r += 1
#
# print ("Mejor configuración:",cantidadServ)
# print()
#
# #--------------------------------------------------------------------------------------------#
#
# # M/D/1
# l = 4
# miu = 6
# Cs = 5 * 7
# Cw = 10 * 7
# m = 1
#
# Lq = (l**2)/(2*miu*(miu-l))
# Wq = l/(2*miu*(miu-l))
# L = Lq + (l/miu)
# W = Wq + (1/miu)
# CT = (m * Cs+ l*W*Cw)
#
# print("M/D/1")
# print ("Lq(Tamaño promedio de la cola):",round(Lq,5)) # Tamaño promedio de la cola
# print ("Wq(Promedio de tiempo en espera en la cola):",round(Wq,5)) # Promedio de tiempo de espera en la cola
# print ("L(Promedio de personas en el sistem):",round(L,5)) # Promedio de número de personas en el sistema
# print ("W(Promedio de tiempo de espera en el sistema):",round(W,5)) # Promedio de tiempo de espera en el sistema
# print ("CT:", round(CT,3))
# print ()
#
# # M/M/1 PF (Población Finita)
#
# N = 300
# P0 = 0
# l = 37.5
# miu = 6
# n = 0
# x = 0
# while n <= N:
#     x += (factorial(N)/factorial(N-n))*((l/miu)**n)
#     n += 1
# P0 = 1/x
# Lq = N - ((l+miu)/l)*(1-P0)
# L = Lq + (1-P0)
# Wq = Lq/((N-L)*l)
# W = Wq + 1/miu
# print("M/M/1 PF")
# print("P0:", round(P0,5))
# print("Lq:", round(Lq,5))
# print("L:", round(L,5))
# print("Wq:", round(Wq,5))
# print("W:", round(W,5))

# Sistema M/M/1
from math import *

l = 24
miu = 30

L = l/(miu-l)
Lq = (l*l)/(miu*(miu-l))
W = 1/(miu-l)
Wq = l/(miu*(miu-l))
ro = l/miu
P0 = 1-ro

print ("M/M/1")
print ("L:",L)
print ("Lq:",Lq)
print ("W:",round(W,3))
print ("Wq:",round(Wq,3))
print ("Ro:",round(ro,3))
print ("P0:",round(P0,3))
print()


# Sistema M/M/m
l = 4
miu = 5
m = 2

cont = 0
P0 = 0
while (cont <= m-1):
    P0 += (1/factorial(cont))*((l/miu)**cont)
    cont += 1
P0 += (1/factorial(m))*((l/miu)**m)*((m*miu)/((m*miu)-l))
P0 = 1/P0

L = (((l*miu*(l/miu)**m)/(factorial(m-1)*(m*miu-l)**2))*P0) + (l/miu)

W = L/l
Lq = L - (l/miu)
Wq = W - (1/miu)
ro = l/(m*miu)


print ("M/M/m")
print ("L:",round(L,5))
print ("Lq:",round(Lq,5))
print ("W:",round(W,5))
print ("Wq:",round(Wq,5))
print ("Ro:",round(ro,5))
print ("P0:",round(P0,5))
print()

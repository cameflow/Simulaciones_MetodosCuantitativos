##################################
##        AUTOCORRELACION       ##
##################################
from math import *

lst = [0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93, 0.99, 0.15,
        0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88, 0.68, 0.49, 0.05, 0.43,
        0.95, 0.58, 0.19, 0.36, 0.69, 0.87]

m = 0
l = 5
i = 3
N = len(lst)
valoresAEvaluar = []

# Calcular la m
x = 0
while (x<N):
    m += 1
    x = i + ((m + 1) * l)
m -= 1

# Calcular los valores a Evaluar
valoresAEvaluar.append(i)
cont = 0
while (valoresAEvaluar[-1] < N):
    valoresAEvaluar.append(valoresAEvaluar[cont]+l)
    cont += 1
valoresAEvaluar.pop()

# Calcular Pij
r = 0.0
cont = 1
while (cont < len(valoresAEvaluar)):
    r += lst[valoresAEvaluar[cont-1]-1]*lst[valoresAEvaluar[cont]-1]
    cont += 1
Pij = ((1/(m+1))*r)-0.25

# Calcular SigmaPij
SigmaPij = round(sqrt((13*m)+7)/(12*(m+1)),5)

# Calcular Z0
Z0 = round(Pij/SigmaPij,5)

print ("m:",m)
print ("N:",N)
print ("Posiciones a evaluar:",valoresAEvaluar)
print ("Pij:",Pij)
print ("SigmaPij:",SigmaPij)
print ("Z0:",Z0)

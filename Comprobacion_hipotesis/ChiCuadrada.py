# k -> Cantidad de intervalos
# N -> Cantidad de datos
# intervalo -> (Valor máximo entre valor mínimo)/K

from decimal import *
from math import *

k = 0
N = 0
alfa = 0
intervalo = 0
ajuste = False
intervals = []
oiei = []
oieisqr = []
finallist = []


# lst = [0.34,0.90, 0.25, 0.89, 0.87, 0.44, 0.12, 0.21, 0.46, 0.67, 0.83, 0.76,
#        0.79, 0.64, 0.70, 0.81, 0.94, 0.74, 0.22, 0.74, 0.96, 0.99, 0.77, 0.67,
#        0.56, 0.41, 0.52, 0.73, 0.99, 0.02, 0.47, 0.30, 0.17, 0.82, 0.56, 0.05,
#        0.45, 0.31, 0.78, 0.05, 0.79, 0.71, 0.23, 0.19, 0.82, 0.93, 0.65, 0.37,
#        0.39, 0.42, 0.99, 0.17, 0.99, 0.46, 0.05, 0.66, 0.10, 0.42, 0.18, 0.49,
#        0.37, 0.51, 0.54, 0.01, 0.81, 0.28, 0.69, 0.34, 0.75, 0.49, 0.72, 0.43,
#        0.56, 0.97, 0.30, 0.94, 0.96, 0.58, 0.73, 0.05, 0.06, 0.39, 0.84, 0.24,
#        0.40, 0.64, 0.40, 0.19, 0.79, 0.62, 0.18, 0.26, 0.97, 0.88, 0.64, 0.47,
#        0.60, 0.11, 0.29, 0.78]

lst = [0.594, 0.928, 0.515, 0.055, 0.507, 0.351, 0.262, 0.797, 0.788, 0.442, 0.097, 0.798, 0.227, 0.127, 0.474, 0.825, 0.007, 0.182, 0.929, 0.852]


N = len(lst)
k = ceil(round((log10(len(lst)) / log10(2.0)),2))
intervalo = round(((max(lst)-min(lst))/k),10)

# Ajuste del intervalo
while (ajuste == False):
    if(max(lst)>(intervalo*k)):
        sIntervalo = str(intervalo)
        decimales = 0
        for i in sIntervalo:
            if (i != '.'):
                sIntervalo = sIntervalo[1:]
            else:
                sIntervalo = sIntervalo[1:]
                decimales = len(sIntervalo)
                break
        newIntervalo = intervalo + 1*10**(decimales*-1)
        intervalo = round(newIntervalo,decimales)
    else:
        ajuste = True

cont = 0
r = 0
while (cont < k):
    intervals.append((r,round((r+intervalo),10)))
    r = round(r+intervalo,10)
    cont += 1

oi = [0]*len(intervals)

for i in lst:
    for x in intervals:
        (menor,mayor) = x
        if((i>menor) & (i<=mayor)):
            oi[intervals.index(x)] += 1

# Revisar si hay menos de 5 dentro de un rango
for i in oi:
    if (i<5):
        if ((oi.index(i) > 0) & (oi.index(i) < len(oi))):
            anterior = oi[oi.index(i)-1]
            siguiente = oi[oi.index(i)+1]
            if(anterior < siguiente):
                oi[oi.index(i)-1] += i
                oi.pop(oi.index(i))
                (menor,mayor) = intervals[oi.index(i)]
                (menor2,mayor2) = intervals[oi.index(i)-1]
                intervals[oi.index(i)-1] = (menor2,mayor)
                intervals.pop(oi.index(i))
            else:
                (menor,mayor) = intervals[oi.index(i)]
                (menor2,mayor2) = intervals[oi.index(i)+1]
                intervals[oi.index(i)+1] = (menor,mayor2)
                intervals.pop(oi.index(i))
                oi[oi.index(i)+1] += i
                oi.pop(oi.index(i))
        elif (oi.index(i) == len(oi)):
            oi[oi.index(i)-1] += i
            oi.pop(oi.index(i))
            (menor,mayor) = intervals[oi.index(i)]
            (menor2,mayor2) = intervals[oi.index(i)-1]
            intervals[oi.index(i)-1] = (menor2,mayor)
            intervals.pop(oi.index(i))

        else:
            (menor,mayor) = intervals[oi.index(i)]
            (menor2,mayor2) = intervals[oi.index(i)+1]
            intervals[oi.index(i)+1] = (menor,mayor2)
            intervals.pop(0)
            oi[oi.index(i)+1] += i
            oi.pop(0)

k = len(intervals)
# ei = [round(N/k,2)] * len(intervals)
ei = [round((1/k)*100,2)]* len(intervals)



for i in oi:
    oiei.append(round(i-ei[oi.index(i)],10))

for i in oiei:
    oieisqr.append(round(i**2,3))

for i in oieisqr:
    finallist.append(round(i/(ei[oieisqr.index(i)]),3))

finalres = 0
for i in finallist:
    finalres += i

finalres = round(finalres,2)



# Imprimir todos los valores
print ("Intervalos:     ",intervals)
print("Frecuencia:      ",oi)
print ("EI:            ",ei)
print ("Oi-Ei:           ",oiei)
print ("(Oi-Ei)^2:      ",oieisqr)
print ("(Oi-Ei)^2/Ei:       ",finallist)
print ("X2:         ",finalres)

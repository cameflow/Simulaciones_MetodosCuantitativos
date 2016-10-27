##################################
##            M/D/1             ##
##################################

l = 4 #Llegadas por periodo de tiempo
miu = 5 #Cuantos se atienden en el periodo
Cs = 5 * 7
Cw = 10 * 7
m = 1

Lq = (l**2)/(2*miu*(miu-l))
Wq = l/(2*miu*(miu-l))
L = Lq + (l/miu)
W = Wq + (1/miu)
CT = (m * Cs+ l*W*Cw)

print("M/D/1")
print ("Lq(Tamaño promedio de la cola):",round(Lq,5)) # Tamaño promedio de la cola
print ("Wq(Promedio de tiempo en espera en la cola):",round(Wq,5)) # Promedio de tiempo de espera en la cola
print ("L(Promedio de personas en el sistem):",round(L,5)) # Promedio de número de personas en el sistema
print ("W(Promedio de tiempo de espera en el sistema):",round(W,5)) # Promedio de tiempo de espera en el sistema
print ("CT:", round(CT,3))
print ()

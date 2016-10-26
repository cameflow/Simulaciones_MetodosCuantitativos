###########################################
##      MÉTODO DE CONGRUENCÍA MIXTO      ##
###########################################

#------- Declaración de Variables -------------#
# semilla -> Número por el que se empieza X0
# cantNumeros -> Cantidad de números aleatorios que se van a generar
# a -> el multiplicador (a>0)
# c -> constante aditiva (c>0)
# m -> el modulo (m>X0, m>a y m>c)
semilla = 27
cantNumeros = 100
a = 8
c =  47
m = 100

listaNumeros = []
repite = False
valorRep = 0
periodo = 0
cola = 0
ciclo = 0

cantAleatorios = 0
listaNumeros.append(semilla)
#-------- Generación de números aleatorios ---------#
while (cantAleatorios < cantNumeros):
    xn = (a * semilla + c) % m

    if ((len(listaNumeros)!=0) & repite == False):
        cont = 1
        for i in listaNumeros:
            if(i == xn):
                repite = True
                valorRep = i
                cola = listaNumeros.index(i)
                ciclo = cantAleatorios - cont
                periodo = cola + ciclo
            cont += 1
    listaNumeros.append(xn)
    semilla = xn
    cantAleatorios += 1



cont3 = 0
for i in listaNumeros:
    print ("X"+ str(cont3)+": "+ str(i))
    cont3 +=1
print ("Valor repetido: " + str(valorRep))
print ("Cola: "+str(cola))
print ("Ciclo: "+str(ciclo))
print ("Periodo: "+str(periodo))

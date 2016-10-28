###########################################
##        MÉTODO DE CUADRADO MEDIO       ##
###########################################

semilla = 4380
numeros = 100
listofnum = []
cola = 0
ciclo = 0
periodo = 0
existe = False
cont = 0
valor = 0
cont2 = 1

#-------Generación de los números aleatorios-------#
while (cont < numeros):
    xn = (semilla)*(semilla)
    tam = len(str(xn))
    x = str(xn)
    if(tam%2 != 0):
        x = "0" + x
    while (len(x)>4):
        n = x[1:]
        r = n[:-1]
        x = r

    if((len(listofnum) != 0) & existe == False):
        for i in listofnum:
            if (int(x) == i):
                existe = True
                valor = i
                cola = listofnum.index(i)
                ciclo = cont - cont2
                periodo = cola + ciclo
            cont2 += 1
        cont2 = 0


    listofnum.append(int(x))
    semilla = int(x)
    cont += 1

cont3 = 0
for i in listofnum:
    cont3 +=1
    print ("X"+ str(cont3)+": "+ str(i))
print ("Valor repetido: " + str(valor))
print ("Cola: "+str(cola))
print ("Ciclo: "+str(ciclo))
print ("Periodo: "+str(periodo))

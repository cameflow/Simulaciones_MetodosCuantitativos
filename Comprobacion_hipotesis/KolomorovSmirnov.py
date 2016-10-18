##################################
##      KOLOMOROV-SMIRNOV       ##
##################################

lst = [0.05,0.14,0.44,0.81,0.93]
lstR = sorted(lst)
lstDplus = []
lstDmin = []
D = 0
Dalfa = 0.565

cont = 1
for i in lstR:
    x = (cont/len(lstR)) - i
    lstDplus.append(round(x,2))
    cont += 1

cont = 1
for i in lstR:
    x = i - ((cont-1)/len(lstR))
    lstDmin.append(round(x,2))
    cont += 1

D = max(max(lstDplus),max(lstDmin))

print("ListR: ",lstR)
print("ListD+: ",lstDplus)
print("ListD-: ",lstDmin)
print("D: ",D)

if (D < Dalfa):
    print("Es uniforme")
else:
    print("No es uniforme")

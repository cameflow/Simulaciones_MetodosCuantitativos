##################################
##           M/M/1 PF           ##
##################################

N = 300 #Cantidad de población total
l = 4 #Llegadas por periodo de tiempo
miu = 5 #Cuantos se atienden en el periodo

P0 = 0
n = 0
x = 0
while n <= N:
    x += (factorial(N)/factorial(N-n))*((l/miu)**n)
    n += 1
P0 = 1/x
Lq = N - ((l+miu)/l)*(1-P0)
L = Lq + (1-P0)
Wq = Lq/((N-L)*l)
W = Wq + 1/miu
print("M/M/1 PF")
print("P0:", round(P0,5))
print("Lq:", round(Lq,5))
print("L:", round(L,5))
print("Wq:", round(Wq,5))
print("W:", round(W,5))

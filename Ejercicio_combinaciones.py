# Calculo de la combinatoria de dos numeros
    
fact_M=1
fact_N=1
fact_MN =1   
# Entradas
ve_M=int(input("Digite M: "))
ve_N=int(input("Digite N: "))

# Calcuar el factorial de M :
for i in range(1,ve_M+1,1):
    fact_M=fact_M*i
    
# Calcular el facotorial de N
vp_conRepWhile=1
while(vp_conRepWhile<=ve_N):
    fact_N=fact_N*vp_conRepWhile
    vp_conRepWhile=vp_conRepWhile+1

# Calcular el factorial de M-N
vp_difMN=ve_M-ve_N
for j in range(1,vp_difMN+1,1):
    fact_MN=fact_MN*j

# Calcular la combinatoria 
vps_comb_MN=fact_M/(fact_N*fact_MN)

# Salidas
print("Factorial de M es: ", fact_M)
print("Factorial de N es: ", fact_N)
print("Factorial de M-N es: ", fact_MN)
print("La combinatoria de M,N es: ", vps_comb_MN)
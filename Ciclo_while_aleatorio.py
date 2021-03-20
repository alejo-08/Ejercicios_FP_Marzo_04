# Librerias usadas en el ejercicio
import random

# Ejercicio 2

# Declarar variables 

cantidadnumeros=1
contadorRepeticiones=0
numero=0
acumuladorSumaTodosNumeros=0 
acumuladorSumaNumerosPositivos=0
acumuladorSumaNumerosNegativos=0

# Entradas
cantidadnumeros= int(input("Digite la cantidad de numeros:"))
#Procesos
while contadorRepeticiones<cantidadnumeros:
    numero=random.randint(-100,100) # Generamos numero aleatorio 
    print("numero: ",numero)
    acumuladorSumaTodosNumeros=acumuladorSumaTodosNumeros+numero
    if numero>0:
        acumuladorSumaNumerosPositivos=acumuladorSumaNumerosPositivos+numero
    else:
        acumuladorSumaNumerosNegativos=acumuladorSumaNumerosNegativos+numero
    contadorRepeticiones=contadorRepeticiones+1
# Fin del ciclo

# Salida de resultados
print("Suma todos: ", acumuladorSumaTodosNumeros)
print("Suma positivos: ", acumuladorSumaNumerosPositivos)
print("Suma negativos: ", acumuladorSumaNumerosNegativos)
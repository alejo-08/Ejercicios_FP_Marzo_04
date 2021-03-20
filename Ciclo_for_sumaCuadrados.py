# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:58:56 2021

@author: cebal
"""

# Programa que calcula el cuadro de los primeros 100 números

# Area de declaraciion de variables
cuadradoNumero= 0
acumuladorSuma= 0

#Entrada
cantidadnumeros= int(input("Digite la cantidad de numeros:"))
# Procesos
#Ciclo para de 1 hasta 100
for num in range(cantidadnumeros+1):
    cuadradoNumero= num*num
    acumuladorSuma= acumuladorSuma+cuadradoNumero
    print("El cuadrado de: ", num, "es :", cuadradoNumero)
    print("La suma acumulada es:", acumuladorSuma)
# Fin del ciclo

print("La suma de los cuadrados es: ", acumuladorSuma)
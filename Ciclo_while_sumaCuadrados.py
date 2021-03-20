# Cilco while 
# Declaracion de variables 
contadorRepeticiones= 1
cuadradoNumero=0
acumuladorSuma= 0
cantidadNumeros=0

# Entradas
cantidadnumeros= int(input("Digite la cantidad de numeros:"))
# P Procesos
while contadorRepeticiones<=cantidadnumeros:
    cuadradoNumero=pow(contadorRepeticiones,2)
    acumuladorSuma+=cuadradoNumero
    print("El cuadrado de: ",contadorRepeticiones, "es :", cuadradoNumero)
    print("La suma acumulada es: ", acumuladorSuma)
    contadorRepeticiones=contadorRepeticiones+1
# Fin while

# Salida
print("la suma de los cuadrados es: ", acumuladorSuma)



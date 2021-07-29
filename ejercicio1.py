import time
numero = int(input("Escriba un número    0 para salir: "))
suma=0
while (numero != 0):
    suma+=numero
    numero = int(input("Escriba un número: "))
print(suma)
time.sleep(10)
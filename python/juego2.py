"""Adivina el numero."""

from random import randint

numero_aleatorio = randint(1,10)

print("Adivina el numero entre el 1 y 10.\n")

mi_numero = int(input("Numero: "))

while mi_numero != numero_aleatorio:
    print("El numero es incorrecto.")
    if mi_numero < numero_aleatorio:
        print(" El numero es mas grande.")
    else:
        print("El numero es mas pequeño.")

    mi_numero = int(input("Numero"))

print("Ganaste")
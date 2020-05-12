"""Juego para adivinar el numero aleatorio"""

from random import randint
numero_random = randint(1,10)

print("Adivina el numero entre el 1 y 10.\n")


mi_numero = int (input("Numero"))


if mi_numero == numero_random:
    print("Ganaste")
else:
    print("Perdiste :c\nEl numero era: {}".format(numero_random))
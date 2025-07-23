# adivina el número
import random

numero_elegido = random.randint( 1, 10) # randint para seleccionar el rango

numero_usuario = int(input("Adivina el número enteroentre 1 y 10: "))

if numero_usuario == numero_elegido:
    print("¡Felicidades! Has adivinado el número.")
else:
    print("Fallaste, era el número", numero_elegido)


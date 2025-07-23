# girar la moneda
import random

def girar_moneda():
    resultado = random.choice(["Cara", "Cruz"])  # Elegir aleatoriamente entre "Cara" y "Cruz"
    return resultado

print(girar_moneda())

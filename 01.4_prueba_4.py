# contador de letras

frase = input("Introduce una frase: ")

caracteres_contador = len(frase)

letras_contador = len(frase.replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", ""))
#.replace para cambiar cosas por otras. o como aqui para eliminar lo no deseado


contador_palabras = len(frase.split())  # .split() para separar palabras por espacios

contador_frases = frase.count(".") + frase.count("!") + frase.count("?")  # .count() para contar ocurrencias de un carácter

print("Has escrito:", caracteres_contador, "caracteres.")
print("Has escrito:", letras_contador, "letras.")
print("Has escrito:", contador_palabras, "palabras.")
print("Has escrito:", contador_frases, "frases.")

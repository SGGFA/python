# creador de contraseñas
import random

my_list = ["q", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ñ", "z", "x", "c", "v", "b", "n", "m"]
print(my_list)
my_n_list = ["Q", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "Z", "X", "C", "V", "B", "N", "M"]
print(my_n_list)
my_s_list = ["<", ">", "!", "@", "·", "¿", ",", ";", ":", "_", "-", "¡", "&", "%", "$"]
print(my_s_list)
c_final = []

i = 0
a = 0

longitud_contraseña = int(input("Pon el numero de caracteres que quieres que tenga tu contraseña: "))


while i < longitud_contraseña:
    c = random.randint(0, 3) # 0=minuscula 1=mayuscula 2=numero 3=simbolo
    i += 1
    print("c es", c)

    if c == 0:
        a = random.choice(my_list)

    elif c == 1:
        a = random.choice(my_n_list)

    elif c == 2:
        a = random.randint(0, 9)
    
    elif c == 3:
        a = random.choice(my_s_list)
    
    c_final.append(a)

print("Los caracteres de tu contraseña son:", c_final)








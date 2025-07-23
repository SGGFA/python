# variables

my_string_variable = "Hello, World!"
print(my_string_variable)

print(" ")

my_int_variable = 14
print(my_int_variable)

print(" ")

my_bool_variable = True
print(my_bool_variable)

print(" ")


print(my_string_variable, my_int_variable)

print(2 + my_int_variable) # (2+14) = 16
print(2, my_string_variable) # la coma para separar valores y imprimirlos juntos

print(" ")


my_int_to_str_variable = str(my_int_variable)  # Convertir int a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

print(" ")

#funciones del sistema (algunas)
print(len(my_string_variable))  # Longitud de la cadena
print(my_string_variable.upper())  # Convertir a mayúsculas
print(my_string_variable.lower())  # Convertir a minúsculas

print(" ")

#como crear multiples variables en una sola linea
nombre, apellido, edad = "Sergio", "García", 14
print("Me llamo:", nombre, apellido,"y tengo", edad, "años.")


address: str = "Calle Falsa 123" #si añades ": str" fuerza el tipo de dato a string(o al que quieras). Pero solo en esa línea
# eso tiene más sentido en los input
address = 32 # si cambias el valor, cambia el tipo de dato
print(type(address)) # ahora es un int
print(address)
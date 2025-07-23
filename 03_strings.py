### Strings ###

my_string = " Mi String"
my_other_string = "Mi otro String"

print(len(my_string))  # Longitud de la cadena
print(len(my_other_string)) 

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # \n para salto de línea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # \t para tabulación
print(my_tab_string)

my_scape_string = "\tEste es \nun String con\\t escapado"
print(my_scape_string)

#Formateo

name, surname, age = "Sergio", "García", 222

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) # %s para letras. %d para numeros
print("Mi nombre es", name, surname, "y mi edad es", age)
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetando de caracteres
language = "Python"
a, b, c, d, e, f = language # cada variable se queda con una letra almacenada
print(a)
print(b)
print(e)

#division
language_slice = language[1:3] #para poner que letras en un rango
print(language_slice)

language_slice = language[0:6]
print(language_slice)

language_slice = language[1:] # si esta vacio es hasta el final
print(language_slice)

language_slice = language[-2] #la letra contando al reves
print(language_slice)

language_slice = language[2]
print(language_slice)

#girar la palabra

reversed_language = language[::-1]
print(reversed_language)



#funciones

print(language.capitalize()) #1º letra en mayuscula
print(language.upper) # todo en mayuscula
print(language.count("t")) #cuenta la letra/num que pongas
print(language.count("pth")) #cuenta la letra/num que pongas  o conjunto, no se tratan por separado
print(language.count("th")) 
print(language.isnumeric())
print("1".isnumeric())
print(language.lower()) #todo minusculas
print(language.upper().isupper()) #isupper para comprobar que este en mayuscula
print(language.lower().isupper())
print(language.startswith("Py")) # el texto empieza con__ (se diferencias mayus de minusculas)
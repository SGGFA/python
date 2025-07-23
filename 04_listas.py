#listas

my_list = list() # 2 formas de declarar una lista
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"] #se pueden mezclar tipos de datos

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0]) #se empieza a contar en 0
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])

print(my_other_list[-1]) #acceder en orden inverso (aqui se empieza a contar desde el 1)


print(my_other_list.count("Brais")) #cuenta en nº de veces que lo que pones esta en la lista
print(my_list.count(30))

print(len(my_other_list))
print(my_other_list.__len__())



age, height, name, surname = my_other_list # cada valor de la lista se asigna a cada variable (se tiene que crear una variable para cada valor de la lista para que funcione)
print(age)

print(my_list[0] + my_list[1]) #suma los elementos indicados

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] #asigna la variable con el valor en ese indice
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list) da error

my_other_list.append("SGdev") #insertas el elemento al final
print(my_other_list)

my_other_list.insert(1, "Rojo") #insertas en el numero que indiques 
print(my_other_list)

my_other_list[1] = "Green" # cambias el valor
print(my_other_list)

my_other_list.remove("Green")
print(my_other_list)

my_list.remove(30) # si hay valores repetidos borra el primero que coincida
print(my_list)

print(my_list.pop()) #borra el ultimo dato(si le pones print te dice cual ha eliminado)
print(my_list)

print(my_list.pop(2)) # borra el dato que haya en el indice (en este caso el 2)
print(my_list)


my_pop_element = my_list.pop(0) # asi puedes guardar aparte el n borrado
print(my_pop_element)
print(my_list)

del my_list[2] # tambien  borra datos, el indice que le indiques entre "[]"
print(my_list)

my_new_list = my_list.copy() #iguala la 1º a la 2º

my_list.clear() #borra toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # da la vuelta al orden de la lista, el reverse no funciona si esta dentro del print
print(my_new_list)

my_new_list.sort() # ordena, si lo dejas sin condiciones dentro lo hace alfabeticamente (solo puede ordenar datos del mismo tipo(o ns si puede entre diferentes numericos))
print(my_new_list)

my_new_list.insert(1, 30)
print(my_new_list[1:2]) # con los ":" te dice que hay entre los indices que pongas
print(my_new_list[1:3])



my_list = "Hola Python" #pasa de lista a string
print(my_list)
print(type(my_list))
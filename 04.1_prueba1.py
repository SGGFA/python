# arreglar la lista

my_list = list()
my_list = [5, 3, 8, 5, 2, 3, 9, 1, 4, 7, 3, 2]

i = 0
print(i)

my_list.sort()
print(my_list)

while i < len(my_list):

    if my_list.count(i) > 1:
        print(my_list)
        my_list.pop(i)
        print(my_list)
    else:
        i = i+1
        print(i)

print(my_list)

my_list.reverse()
print(my_list)



#datos de pantalla
print("El N mayor es", my_list[0])
print("El N menor es", my_list[-1])
print("La media es", sum(my_list)/len(my_list))

media = sum(my_list)/len(my_list)


my_new_list = my_list.copy()
print(my_new_list)

i = 0
print(i)

while i < len(my_new_list):

    if my_new_list[i] < media:
        print(my_list)
        my_list.pop(i)
        print(my_list)
    else:
        i = i+1
        print(i)

print(my_new_list)
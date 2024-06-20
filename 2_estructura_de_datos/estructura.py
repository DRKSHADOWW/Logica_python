# Liatas
my_list = ["andres", "David", "Murillo"]

print(my_list)
my_list.append("Ballestero") # Insercción
print(my_list)
my_list.remove("andres") # Eliminación
print(my_list)
print(my_list[1]) # Acceso
my_list[1] = "gabriel" # Actualización
print(my_list)
my_list.sort() #Ordenacion
print(my_list)

#Tuplas -son inmutables
my_tuple = ("andres", "david", "@Murillo", '31')
print(my_tuple[1]) # Acceso
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

#sets -no se puede acceder al set - evita duplicados - trabaja en desorden

my_set = {"andres", "david", "@Murillo", '31'}
print(my_set)
my_set.add("andresdavid1305@hotmail.com")
print(type(my_set))
my_set.remove("andres")
print(my_set)
set = sorted(my_set) # No se puede ordenar
print(set)

#Diccionario

my_dict = {
    "name": "Andres",
    "apellido": "Murillo",
    "edad": 31,
    "email": "andresdavid1305@hotmail.com",
    "hobbies": ["futbol", "leer", "programar"]
}
my_dict['alias'] = "corneto" #Insercción 
print(my_dict)
print(my_dict["name"])  #Acceso
my_dict["edad"] = "37" # Actualización
print(my_dict)
print(type(my_dict))
del my_dict(["apellido"]) # Eliminación


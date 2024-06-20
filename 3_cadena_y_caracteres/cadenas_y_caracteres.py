#-------- Operaciones --------

#Variables a Usar
s1 = "Hola"
s2 = "soy Andrés"

# Concatenación
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2])

# Longitud
print(len(s1))

#Slicing (porción)
print(f"Slicing {s1[2:5:-1]}") # se agrega : indica recorrido al reves
print(f"Slicing {s1[5:]}")
print(f"Slicing {s2[0:2]}")
print(f"Slicing {s2[:2]}")

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("Hola", "Adiós"))

# División
print(s1.split("o"))

# mayúculas y minúsculas
print(s1.upper())
print(s1.lower())
print("andres murillo".title())
print("andres murillo".capitalize())

# Eliminación de espacios al principio y al final
print(" andres murillo ".strip())

# Busqueda al principio y al final
print(s1.startswith("la"))
print(s1.startswith("Ho"))
print(s1.endswith("Ho"))
print(s1.endswith("la"))

# Busqueda de posición
print("hola, solo quiero programar".find("la"))
print("hola, solo quiero programar".lower().find("la"))

# Busqueda de ocurrencias
print(s1.lower().count("a"))

# formatear cadena interpolación
print(f"{s1} , {s2}")

# Transformación  de lista de caracteres
print(list(s1))

# Transformación de listas en cadena
l1 = [s1, ",", s2, "!"]
print(" ".join(l1))

# Transformaciones númericas
s4 = "1234566"
s4 = int(s4)
print(type(s4))

# varias Comprobraciones
print(s4.is_integer())
print(s1.isalnum())
print(s1.isalpha())

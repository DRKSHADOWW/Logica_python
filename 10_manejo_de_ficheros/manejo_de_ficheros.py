import os

# Desarrola un programa capaz de crear un archivo que se llame como tu usuario de github
# y tenga la extensión .txt.
# Añade varias lineas a ese fichero:
#- tu nombre
#-edad
#-lenguaje de programación favorito
#- imprime el contenido
#- borra el fichero

file_name = "andres.txt"
with open(file_name, "w") as file:
    file.write("Hola, soy Andrés")
    
with open(file_name, "r") as file:
    print(file.read())
    
os.remove(file_name)

# Desarrola un programa de getion de vnta que almacene sus datos en un archivo txt.
#- cada producto se guarda en una línea del archivo de la siguiente manera:
#[nombre_producto], [cantidad_vendida], [precio].
#- siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, 
#eliminar productos y salir.
#- También debe poseer opciones para calcular la venta total y por producto.
# la opción salir borra el .txt.


    
    
    
file_producto = "Producto.txt"

while True:
            
    print("1. Añadir producto: ")
    print("2. Consultar producto: ")
    print("3. Actualizar producto: ")
    print("4. Borrar producto: ")
    print("5. mostrar producto: ")
    print("6. calcular venta pro producto: ") 
    print("7. Salir")
    
    option = input("Selecciona una opción: ")  
            
            
    match option: 
        case "1":
            name = input("Nombre del producto: ")
            quantity = input("cantidad del producto: ")
            price = input("Precio del producto: ")
            
            with open(file_producto, "a") as file:
                file.write(f"{name}, {quantity}, {price} \n")
                            
                          
        case "2":
            name = input("Nombre del producto: ")
            with open(file_producto, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        break
                    else:
                        print("No existe el producto")
            
        case "3":
            name = input("Nombre : ")
            quantity = input("cantidad : ")
            price = input("Precio : ")
            
            with open(file_producto, "r") as file:
                lines = file.readlines()
            with open(file_producto, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {quantity}, {price}\n")
                    else:
                        file.write(line)
                
                    
            
            
        case "4":
            name = input("Nombre : ")
            with open(file_producto, "r") as file:
                lines = file.readlines()
            with open(file_producto, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)
                   
        case "5":
            with open(file_producto, "r") as file:
                print(file.read())
        case "6":
            total = 0
            with open(file_producto, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(total)
        case "7":
            if option == "7":
                os.remove(file_producto)
                break
            else:
                print("Opcion invalida")    
                
           
        
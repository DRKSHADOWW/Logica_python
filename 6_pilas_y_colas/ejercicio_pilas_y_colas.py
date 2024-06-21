# Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atras
# de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#las palabras "Adelante", "atrás" desencadenan esta acción, el resto se interpreta como el nombre de una nueva web.

def navegar():

    stack = []
    
    while True:
        action = input("adelante / atrás / salir:  ")
        if action == "salir":
          print("Saliendo del navegador: ")
          break
        elif action == "adelante":
            pass
        elif action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
          stack.append(action)
          
        if len(stack) > 0:
            print(f"Has navegado a la web: {stack[len(stack) -1]}.")
        else:
            print("Estás en la página de inicio")
#navegar()

#Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una impresora compartida que recibe documentos y los imprime cuando así se le indica.
# La palabra "Imprimir" imprime un elemento de las cola, el resto de la palabras se interprestan como nombres de documentos.

def printer():
    queue = []
    while True:
        action = input("documento / imprimir / salir: ")
        if action == "salir":
            print("Saliendo de la impresora: ")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print("No hay documentos en la cola")
        else:
            queue.append(action)
    
printer()
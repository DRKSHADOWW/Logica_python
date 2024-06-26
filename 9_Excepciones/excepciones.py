#Ejercicio:
# EXplora el concepto de manejo de excepciones según en lenguaje.
#fuerza un error en tu código, captura el error, imprime dicho error
# y evita que el progrma se detenga de manera inesperada.
#prueba dividir "10/0" o acceder a un índice no existente
# de un listado para intentar provocar un error.


try:
    print([1, 2, 3, 4][4])
    print(10/0) 
    
except Exception as e:
    print(f"Ha ocurrido un error: {type(e).__name__}")
    
finally:
    print("El programa sigue funcionando...")
    
    
    
#Crea una función que se acapaz de procesar parámetros, pero también
#pueda lanzar 3 tipos diferentes de excepciones ( una de ellas tiene que corresponderse 
#con un tipo de excepciones creada por nosotros de manera personalizada, y debe ser lanzada de manera manual) en caso de error.
#- Captura todas las excepciones desde el lugar donde llamas a la función.
#- Imprime el tipo de error y el mensaje de error.
#- imprime si no se ha producido algún error.
#- Imprime que la ejecución ha finalizado.

# (type(e).__name__)  == muestra el error expecífico


class StrTypeError(Exception):
    pass

def process_params(parameters: list):
    
    
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto.")
    else:
        print("Finalizo ejecución")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)
    
    
    try:
        process_params([1,2,3,4])
    except IndexError as e:
        print(f"El número de elementos de la lista debe ser mayor que dos. {e}")
    except ZeroDivisionError as e:
        print(f"El segundo elemento de la lista no puede ser un cero {e}") 
    except StrTypeError as e:
        print(f"{e}")   
    except Exception as e:
        print(f"Se ha priducido un error inesperado: {e}")
    else:
        print("No se ha producido ningún error.")  
    finally:
        print("La ejecución ha finalizado.")
    
    
process_params([1,2,3,4])
    

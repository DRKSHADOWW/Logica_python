#Funciones definidas por el usuario

#simple

def saludo():
    print("Función simple")
    
saludo()

#Con retorno

def return_saludo():
    return "función con retorno "
saludo_retorno = return_saludo()
print(saludo_retorno, "definida en variable")
print(return_saludo(), "llamando directamente la funcion")


def funtcion_argumento(arg , arg2 ):
    print(f" Con argumentos: {arg2}, {arg}")
    
funtcion_argumento("ARGUMENTOS", "argumento2")

#Con argumento predeterminado
def funtcion_argumento_predeterminado(arg = "default" , arg2 = "predeterminado"):
    print(f"función con argumento predeterminado, {arg}, {arg2}")
    
funtcion_argumento_predeterminado(arg2="andres")

#con argumentos y return

def return_args_greet(greet, name):
    return f"con argumentos y return {greet}, {name}!"

print(return_args_greet("hi", "andres"))

# Con retorno de varios valores


def multiple_return_greet():
    return "hi", "andres", "!"

saludo, nombre, i = multiple_return_greet()
print(f"multiples valores en return {saludo}, {nombre}, {i}")

#Con un número varible de argumentos
def variable_args_greet(*names):
    for name in names:
        print(f"hola, {name} ")
        
variable_args_greet("python", "brais", "andres")



# Con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f'Hola, {value} ({key})')
        
        
variable_key_arg_greet(valor_numerico=3, valor_string="valor cadena")

# Funciones dentro de funciones


def outer_function():
    def inner_function():
        print("dentro de una función, se ejecuta si se llama")
    
    inner_function()
outer_function()

#Funciones del lenguaje(builtin)

print(len("Andrés"))
print("Andrés".upper())
print(type(36))

#scope global y scoper local

global_escope = "scope_global"

def function_local():
    local_scope = "scope_local"
    print(f"Escope_local => ejucutando; {global_escope}")
    return local_scope
    
function_local()

    
    
    


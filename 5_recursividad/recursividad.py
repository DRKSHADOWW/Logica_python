
        


# Recursividad = Función que se llama a ella misma 

# Entiende el concepto de recursividad creand un afunción recursica que imprima números del 100 al 0
def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number -1)
    
countdown(10)

# Calcular el factorial de un número concreeto (la función recibe ese número).

def factorial(n: int):
    if n < 0:
        print("Numeros negativos no es valido")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


# Calcular el valor  de un elemento  concreto(según la posición ) en la sucesión de fibonacci (la función recibe la posición)

def fibonacci(n: int) -> int:
    if n <= 0:
        print("numero mayo r a cero: ")
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))


    
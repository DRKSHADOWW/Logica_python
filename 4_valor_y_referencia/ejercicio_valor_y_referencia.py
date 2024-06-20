# Crea dos programas que reciban dos parametros (cada uno) definidos como variabels anteriormente.
#-- Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
# Estos parametros los intercambia entre ellos en su interior, lo retorna, y su retorno se agina a dos variables diferentes a los originales ylas nuevas, comprobando que se ha invertido su valor en las segundas,

# Comprueba también que se ha conservado el valor original en las primeras.



# Por valor

def paramater_value(arg1: int, arg2: int) -> tuple:
    temp = arg1
    arg1 = arg2
    arg2 = temp
    return arg1, arg2
    
valor1 = 10
valor2 =  29

int_f, int_g = paramater_value(valor1, valor2)

print(f"{valor1}, {valor2}")
print(f"{int_f}, {int_g}")

# Por referencia

def paramater_ref(arg1: list, arg2: list) -> tuple:
    temp = arg1 # temp: auxiliar de variable
    arg1 = arg2
    arg2 = temp
    temp.append(50)
    print(temp)
    return arg1, arg2
    
valor1 = [10, 40]
valor2 =  [56, 32]

int_f, int_g = paramater_ref(valor1, valor2)
print(f"{valor1}, {valor2}")
print(f"{int_f}, {int_g}")
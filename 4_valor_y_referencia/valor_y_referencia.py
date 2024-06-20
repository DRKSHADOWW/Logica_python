# Valor y referencia

# Tipos de Datos por Valor
# Los datos por valor son mutables
int_a = 10
int_b = 30
int_a = int_b 

print(int_a)
print(int_b)

# Tipos de dato por referencia
# Los datos se heredan
list_a = [10, 20]
list_b = [30, 40]
list_a.append(list_b)
list_a.append(50)

print(list_a)

#funciones con datos por valor
# dentro de una funcion la variable es scope global no se altera
my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)


my_int_func(my_int_c)
print(my_int_c) 

# Funciones con datos por referencia
#
list_c = [10, 20]

def my_list_func(my_list: list) :
    my_list.append(30)
    
    my_list_d = my_list
    my_list_d.append(40)
    
    print(my_list)
    print(my_list_d)
    
my_list_c = [10, 20]
my_list_func(my_list_c)
print(my_list_c)


    
       

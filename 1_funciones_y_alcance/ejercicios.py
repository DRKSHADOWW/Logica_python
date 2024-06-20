# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for i in range(10, 56):
    if(i % 3 == 0 and i != 16 and i % 2 == 0):
        print(i)
    
#Crea una función que reciba todos los parámetros de tipo cadena de texto y retorne un número.
#- La función imprime todos los numeros del 1 al 100. Teniendo en cuenta que:
# -- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# -- Si el número es múltiplo de 5, muestra la cadena de texto del segundo paraámetro.
# -- Si el número es múltiplo de ambos (3 y 5), muestra la cadena de texto concatenadas.
# -- La función retorna el número de veces que se ha impreso el número en lugar de los textos.


# Este se le conoce como fizz buzz
def get_params(text_1, text_2)-> int:
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(text_1, text_2)
        elif number % 3 == 0:
            print(text_1)          
        elif number % 5 == 0:
            print(text_2)
        else: 
            print(number)
            count += 1
    return count


        
       
           
            
print(get_params("texto 1", "texto 2"))
            



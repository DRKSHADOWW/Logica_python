# Implementa dos clases que representen las estructuras de la Pila Y lCola(estudiadas en el ejercicio número 6 de la ruta de estudio)
#- Deben poder inicializarse y disponer de operaciones para añadir, eliminar, retornar el número de elementos e imprimir todo su contenido


class Stack():
    
    def __init__(self) -> None:
        self.stack = []
    
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    
    def count(self):
        return len(self.stack)
        
    def print(self):
        for item in reversed(self.stack):
            print(item)
            
            
my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
print("---------------------------------")
my_stack.pop()
my_stack.print()
print(my_stack.count())
        
    
    
class Queue():
    def __init__(self):
        self.queue = []
        
    
    
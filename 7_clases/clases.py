class Programmer:
    
    surname: str = None
    
    def __init__(self, nombre, edad , lenguage):
        self.nombre = nombre
        self.edad = edad
        self.lenguage =lenguage
        
        
        
    def print(self):
        print(
            f"Nombre:  {self.nombre} |  Edad: {self.edad} Surname: {self.surname}  |Lenguages: {self.lenguage}")
        

my_programmer = Programmer("Brais", 31, ("Python", "Kotlin", "Swift"))
my_programmer.print()
my_programmer.surname = "Murillo"
my_programmer.print()
my_programmer.edad = 35
my_programmer.print()

 

        
        
        

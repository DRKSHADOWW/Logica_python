#Ejercicio
#Explora el concepto de herencia según tu languaje, Crea un ejemplo que 
#implemente una superclase Animal y un par de subclases Perro  y Gato,
#

class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre
             
    def sound(self):
        pass
        
#Subclases
        
class Dog(Animal):
        
    def sound(self):
        print("Wow")

class Cat(Animal):
        
    def sound(self):
        print("Miau")
        
def print_sound(animal: Animal):
    animal.sound()
    
my_animal = Animal("Animal")
print_sound(my_animal)
my_dog = Dog("Perro")
print_sound(my_dog)
my_cat = Cat("Gato")
print_sound(my_cat)

# Extra

class Employees:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.employees = []
        
    def add(self, employee):
        self.employees.append(employee)
        
    def print_employees(self):
        for employee in self.employees:
            print(employee.name)
        
        
class Manager(Employees):
    def coordnate_projects(self):
            print(f"{self.name} esta coordinando todos los proyectos de la empresa")
   
            
class ProjectManajer(Employees):
    
    def __init__(self, id: int, name: str, project: str):
        super().__init__(id, name)
        self.project = project
    
    def coordnate_projects(self):
        
        print(f"{self.name} esta coordinando su proyecto")
        
     
    
        
class Programmer(Employees):
    def __init__(self, id: int, name: str, language: str):
        super().__init__(id, name)
        self.language = language
        
    def code(self):
        print(f"{self.name} esta programando en {self.language}")
        
    def add(self, employee: Employees):
        print(f"Un programador no tiene empleados a su cargo. {employee.name} no se añadira")
        
        
        
my_manager = Manager(1, "Andres")
my_project_manager = ProjectManajer(2, "Murillo", "Proyecto 11")
my_project_manager2 = ProjectManajer(3, "Ballestero", "Proyecto 13")
my_programmer = Programmer(4, "Kontrol", "Swift")
my_programmer2 = Programmer(5, "Ros", "Cobol")
my_programmer3 = Programmer(6, "Bushi", "Dart")

my_manager.add(my_project_manager)
my_manager.add(my_project_manager2)

my_project_manager.add(my_programmer)
my_project_manager.add(my_programmer2)
my_project_manager2.add(my_programmer3)

my_programmer.add(my_project_manager)

my_programmer.code()
my_project_manager.coordnate_projects()
my_manager.coordnate_projects()
my_manager.print_employees()
my_project_manager.print_employees()
my_programmer.print_employees()


        



    
    
    
# Debes implementar funcionalidades de búsqueda, insercción, actualización y eliminación de contactos
    # --Cada contacto debe tener un nombre y unnúmero de teléfono.
    # --El programa solicita en primer lugar cuál es la operación que se requiere realizar, y a continucación los datos necesarios para llevarla a acabo.
    # --El programa no puede dejar de introducir números de teléfono no númericos y con más de 11 dígitos. (o el número de dígitos que quieras)
    # --Tabién se debe proponer una operación de finalización de programa.



def mi_agenda():
    
    
        agenda = {}
   
   
        def insert():
            phone = input("Ingrese su nuevo numero: ")
            if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:      
                agenda[name] = phone
            else:
                print("debes introducir un número de teléofono con menos dígitos: ")
   
    
        while True:
            
            print("\n     Opciones:  \n")
            
            print("1. ingrese id para busqueda : ")
            print("2. insertar datos: ")
            print("3. Modificar datos: ")
            print("4. Eliminar Datos: ")
            print("5. Salir del programa: \n")
            
            opcion = input("Ingrese Opción: ")
            
            
            match opcion:
                case '1':
                    name = input("Ingrese su nombre: ")
                    if name in agenda:
                        print(f"El telefono  de {name} es {agenda[name]} ")
                    else:
                        print(f" el contacto {name} no existe")
                case '2':
                    name = input("Ingrese su nombre: ")
                    insert()
                    
                    
                case '3':
                    name = input("Ingrese su nombre actualizar: ")
                    if name in agenda:
                        insert()
                            
                        
                    else:
                        print(f"el contacto {name} no existe")    
                
                case '4':             
                    name = input("Ingrese su nombre eliminar: ")
                    if name in agenda:
                        agenda.remove[name]
                    else:
                        print(f"El contacto {name} no existe")
                case '5':
                    break
    
                
            
mi_agenda()
             
            


list_students = {}
temporary_data = {}

def validation_id():
    while True:
        id = input("Ingrese el ID del estudiante: ")
        if not id.isdigit() and len(id) <= 10:
            print("Error: ingresaste texto / id incorrecto")
            continue
        id = int(id)
        if id in list_students:
            print("El ID ya existe. Verifica e ingresa de nuevo")
            continue
        if id < 0:
            print("El ID no puede ser negativo")
            print(f"ID válido")
            temporary_data[id] = id
            
        else:
            break
        
def validation_id_1():
    while True:
        id = input("Ingrese el ID del estudiante: ")
        if not id.isdigit():
            print("Error: ingresa solo numeros, no texto")
            continue
        id = int(id)
        if id < 0:
            print("El ID no puede ser negativo")
            print(f"ID válido")
            temporary_data[id] = id
        else:
            break
            
        
def validation_student():
    while True:
        student = input("Ingrese el nombre del estudiante: ")
        if student.isalpha():
            print(f"Estudiante válido : {student}")
            break
        else:
            print("Error: Ingresa solo letras, no numeros")
            continue
        
def validation_note():
    while True:
        note = input("Ingrese la nota correspondiente: ")
        if not note.isdigit():
            print("Error: ingresa solo numeros, no texto")
            continue
        note = float(note)
        if note < 0.0 or note > 5.0:
            print("ERROR, rango de nota inválida")
            print("La nota debe estar entre 0.0 y 5.0")
            continue
        print(f"Nota válida: {note}")
        break

def validation_old():
    while True:
        old = input("Ingrese la edad correspondiente: ")
        if not old.isdigit():
            print("Error: ingresa solo numeros, no texto")
            continue
        old = int(old)
        if old < 0:
            print("ERROR, La edad no puede ser negativa")
            continue
        print(f"Edad válida: {old}")
        break

def new_students():
    id_correct= validation_id()
    name_correct = validation_student()
    note_correct = validation_note()
    old_correct = validation_old()
    #validate that the id not exist in the list_students
    for item in list_students.values():
        if item["name"].lower() == validation_id.lower():
            print("El ID del estudiante ya existe en la base de datos")
            return
        
        list_students[id] ={"ID":id_correct, "name": name_correct, "notes": note_correct, "old": old_correct}
        print(f"Estudiante {list_students["name"]} ingresado con éxito")
        
        next = input("Desea agregar otro estudiante? s/n: ")
        if next.lower() == "s":
            new_students()
        else:
            print("Regresando al menu principal")
            
def search_students():
    validation_id_1()
    if id in list_students:
        student = list_students[id]
        print(f"ID: {id}, Nombre: {student["name"]},Nota: {student["note"]}, Edad:{student["old"]}")
    else:
        print("Estudiante no encontrado")
        
    next = input("Desea buscar otro estudiante? s/n: ")
    if next.lower() == "s":
        search_students()
    else:
        print("Regresando al menu principal")  

def update_students():
    validation_id_1()
    if id in list_students:
        student= list_students[id]
        print(f"ID: {id}, Nombre: {student["name"]},Nota: {student["note"]}, Edad:{student["old"]}")
        new_note = float(input("Ingrese nuevas notas: "))
        new_old = int(input("Ingrese la nueva edad: "))
        list_students[id]["note"] = new_note
        list_students[id]["old"] = new_old
        print(f"Estudiante {student["name"]} actualizado cion éxito.")
    
    else:
        print("Estudiante no encontrado")
    next = input("Desea actualizar otro estudiante? s/n: ")
    if next.lower() == "s":
        update_students()
    else:
        print("Regresando al menu principal")  

        
def delete_students():
    validation_id_1()
    
    if id in list_students:
        del list_students[id]
        print(f"Estudiante con el ID {id} eliminado con éxito")
    else:
        print("No se encontro el estudiante")
        
    next = input("Desea eliminar otro estudiante? s/n: ")
    if next.lower() == "s":
        delete_students()
    else:
        print("Regresando al menu principal")  

def average_student():
    validation_id_1()
    if id in list_students:
        student= list_students[id]
        print(f"ID: {id}, Nombre: {student["name"]},Notas actuales: {student["note"]}")
    
    student_1 = list_students[id]
    name = list_students["name"]
    note_1 = list_students["note"]
    
    if not note_1:
        print(f"El estudiante no tien notas aún")
        return
    average = sum(note_1) / len(note_1)
    print(f"Estudiante con ID : {student_1}")
    print(f"Con nombre: {name}")
    print(f"Con Notas:{note_1}")
    print(f"El promedio de sus notas es: {average}")


def threshold_students():
    
    for i in list_students["name"]["notes"]:
        if i < 3.0:
            print(i)
        
        else:
            print("No hay estudiantes con notas menores a 3")   
                           
 

def menu():
    while True:
        print("====Menu=====")
        print("1.Agregar estudiantes")
        print("2.Buscar estudiantes")
        print("3.Actualizar informacion de estudiantes")
        print("4.Eliminar estudiantes")
        print("5.Cálcular promedio de notas")
        print("6. Umbral estudiantes notas>3")

        option = input("Ingrese una opcion: ")

        if option.isdigit():
            option = int(option)
            
            if 1 <= option <=6:
                print("Entrada válida, continuamos...")
                break
            else:
                print("Error: solo numeros del 1 al 6")
                
        else: 
            print("Ingresa solo numeros, no texto")
            break
    
    match option:
        case 1:
            print ("=====Agrega un estudiante======")
            new_students()
            
        case 2:
            print ("=====Consultar un estudiante======")
            search_students()
            
        case 3:
            print ("=====Actualizar informacion de un estudiante======")
            update_students()
            
        case 4:
            print ("=====Eliminar un estudiante======")
            delete_students()
            
        case 5:
            print ("=====Calcular promedio de un estudiante======")
            average_student()
            
        case 6:
            print ("=====Umbral de estudiantes======")
            threshold_students()
            
    menu()
    
menu()        
            
          
            
                
            


##declarar una funcion que permita crear una lista de N estudiantes 

def crear_lista_estudiantes(cantidadEstudiantes):
    estudiantes=[]

    for _ in range(cantidadEstudiantes):
      estudiante={}
      estudiante["id"]=input("id: ")
      estudiante["documento"]=input("documento: ")
      estudiante["nombre"]=input("nombre: ")
      estudiante["telefono"]=input("telefono: ") 
      estudiante["promedio"]=input("promedio: ")
      estudiante["semestre"]=input("semestre cursado: ")      
      estudiante["esBecado"]=input("estas becado?: ")
      estudiantes.append(estudiante)
    return estudiantes  

##invocando funcion
lista=crear_lista_estudiantes()      
print(lista) 
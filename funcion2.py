##Tarea una funcion que de forma aleatoria crea una lista de N notas enteras y devuelve esa lista 
import random
def general_lista_notas(CantidadNotas):
    notas = []
    for _ in range(CantidadNotas):
        notas.append(random.randint(1,5))
    return notas   

resultado=general_lista_notas(100)
print(resultado)
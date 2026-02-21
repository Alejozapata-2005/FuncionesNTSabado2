##crear una funcion que resiva una lista de numero enteros y calcule su promedio para retormnarlo 
def calcular_promedio_notas(notas):
     promedio=sum(notas)/len(notas)
     return promedio     


notas=[1,1,2]
print(calcular_promedio_notas(notas))
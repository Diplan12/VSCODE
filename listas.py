import sys


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla 
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

materias =["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    
    for i in materias:
        print(f"YO ESTUDIO "+i )
"""


"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después 
las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es 
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes 
notas introducidas por el usuario.

materias =["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    puntos=[]
    for i in materias:
        nota=int(input(f"NOTA SACADA EN " +i))
        puntos.append(nota)

    for i in range(len(materias)):
        print("EN " +materias[i]+ "has obtenido " + f"{puntos[i]}")"""


"""Escribir un programa que pregunte al usuario los números ganadores 
de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

materias =[]
    numerosLOTO=[]
    for i in range(6):
        nota=int(input(f"NUMEROS GANADORES"))
        numerosLOTO.append(nota)
    numerosLOTO.sort()
    print(numerosLOTO)
"""


"""Escribir un programa que almacene en una lista los números 
del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
numeros=[]
    for i in range(1,11,1):
        numeros.append(i)
        
    numeros.sort(reverse=True)
    print(numeros)
"""


"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

def main():
    materias =["Matemáticas", "Física", "Química", "Historia" , "Lengua"]
    aprobadas=[]
    reprobadas=[]
    for i in materias:
        nota=int(input(f"NOTA SACADA EN " +i))
        if nota > 50:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
        
    print("LAS MATERIAS QUE REPROBASTE FUERON ",reprobadas)
    print("LAS MATERIAS QUE REPROBASTE FUERON ",aprobadas)
    
    
    




    

   
    
if __name__ == '__main__':
    sys.exit(main())
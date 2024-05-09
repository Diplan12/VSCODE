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
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
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
"""


"""Escribir un programa que almacene el abecedario en una lista, elimine de la lista 
las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

#abecedario=[""]
    abecedario = [chr(i) for i in range(97, 123)]
    for i in range(len(abecedario),1,-1):
        if i%3 == 0:
            #print(abecedario[i])
            abecedario.pop(i)

    print(abecedario)  """


"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
     word = input("Introduce una palabra: ")
    reversed_word = word
    word = list(word)
    reversed_word = list(reversed_word)
    reversed_word.reverse()

    print(word)

    if word == reversed_word:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
"""
"""Escribir un programa que pida al usuario una palabra 
y muestre por pantalla el número de veces que contiene cada vocal.

 palabra= input("DIFITE UNA PALABRA")
    letra= input("DIFITE UNA LETRA")
    contador= 0

    for i in range(len(palabra)-1,-1,-1):
        if palabra[i] == letra:
            #print(palabra[i])
            contador +=1
    print("EL TEXTO TIENE "+str(contador)+ f"{letra}")  

    




     palabra= input("DIFITE UNA PALABRA")
    letra= ["a","e","i","o","u"]
    contador= 0

    for i in letra:
        for j in palabra:
            if i==j :
                print("encontrada")
                contador +=1
    
    print ("Texto tiene " + str(contador) )

  word = input("Introduce una palabra: ")
    vocals = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocals: 
        times = 0
        for letter in word: 
         if letter == vocal:
            times += 1
        print("La vocal " + vocal + " aparece " + str(times) + " veces")    
"""
"""Escribir un programa que almacene en una lista los siguientes precios, 
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

 precios=[50, 75, 46, 22, 80, 65, 8]
  max = min = precios[0]
  for number in precios:
    if number < min:
        min = number
    elif number > max:
       max = number
  print("El mínimo es " + str(min)) 
  print("El máximo es " + str(max))
"""
def main():
    print("El mínimo es " + str(min)) 
    print("El máximo es " + str(max))

        
   
    
if __name__ == '__main__':
    sys.exit(main())
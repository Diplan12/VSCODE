
import sys


"""monedas ={'Euro':'€', 
               'Dollar':'$', 
               'Yen':'¥'}
    usuario= input("INTRODUSCA UNA DIVISA: ")
    print(monedas.get(usuario.title(),"NO SE ENCUENTRA"))
    """



"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y l
o guarde en un diccionario. Después debe mostrar
 por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
 
 solucion
 nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
 
 MI SOLUCION 
 datos ={"nombre":"",
            "anos": 0,
            "direccion":"",
            "telefono":0
            }
    nombre= input("INTRODUSCA su nombre: ")
    edad= input("INTRODUSCA su edad: ")
    direccion= input("INTRODUSCA su direccion: ")
    telefono= input("INTRODUSCA su numero: ")

    datos["nombre"]=nombre
    datos["edad"]=edad
    datos["direccion"]=direccion
    datos["telefono"]=telefono

    print(f"{datos['nombre']} tiene {datos['edad']}, vive en {datos['direccion']} y su numero es {datos['telefono']} ")
 
 """


"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

frutas ={"Platano":	  1.35,
              "Manzana":  0.80,
              "Pera"	: 0.85,
              "Naranja"	: 0.70,
            }
    usuario= input("INTRODUSCA LA FRUTA: ")
    libra= int(input("INTRODUSCA el peso: "))
    print("SU PRECIO TOTAL ES DE "+str(frutas.get(usuario.title(),"no tenemos")*libra))

soluucion    
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")

"""

"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa
 y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
 
 meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo',
         6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
   
   feacha= input("INTRODUSCA LA Fecha formato dd/mm/aaaa: ")
   fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
   fecha = fecha.split('/')
   print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
 """

"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, 
y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

  materias= {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    total=0
    for x,y in materias.items():
        print(x,"tiene" ,y,"créditos")
        total +=y
    print("EL TOTAL DE CREDITOS ES ", total)
"""

"""Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

datos= {}
    continuar="si"

    while continuar =="si":
        clave=input("Que dato quieres actualizar: ")
        valor = input(clave+ ":" )
        datos[clave]=valor
        continuar=input("Desea seguir introduciendo datos   si o no?")
    
    print(datos)

"""

"""carrito= {}
    continuar="si"

    while continuar =="si":
        clave=input("Que producto deseas comprar: ")
        valor = input("INTRODUSZCA EL PRECIO DE "+clave+ ":" )
        carrito[clave]=int(valor)
        continuar=input("Desea seguir comprando   si o no?")

    total=0
    print("-----LISTA DE COMPRA----")
    for articulo,precio in carrito.items():
        print(articulo,"VALE  $",precio)
        total +=precio
    print("EL TOTAL DE CREDITOS ES ", total)"""


"""
parte 8 
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
        
        
        
        
def opcion_b():
    print("Has seleccionado la opción B")

def opcion_c():
    sys.exit(main())
    

def main():
    def opcion_a():
        print("Has seleccionado la opción A")
        continuar="si"

        while continuar =="si":
            clave=input("PALABRA EN INGLES: ")
            valor = input("PALABRA"+clave+ " EN ESPANOL =" )
            diccionario[clave]=valor
            continuar=input("Desea AGREGAR otra palabra si o no?")
        
        sys.exit(main())
    
    def opcion_b():
     print("Has seleccionado la opción B")
     palabra=input("PALABRA EN INGLES ").lower
     print("SU TRADUCCION ES "+ diccionario[palabra])

    def opcion_c():
        sys.exit(exit)
    
    
    
    diccionario={}
    opciones = {
    "a": opcion_a,
    "b": opcion_b,
    "c": opcion_c
}
    print("---------MENU----------")
    print("OPCION A (INTRODUCIR UNA PALABRA AL DICCIONARIO)")
    print("OPCION B (BUSCAR UNA PALABRA DE ESPAÑOL A INGLES ")
    print("OPCION C (SALIR)")
    
    opcion = input("Selecciona una opción (a, b, c): ").lower() 
    if opcion in opciones:
        opciones[opcion]()
    else:
        print("Opción no válida")"""



def main():
 diccionario = {}
 palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
 
 for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor

 frase = input('Introduce una frase en español: ')
 for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
    


if __name__ == '__main__':
    sys.exit(main())
import sys


"""Echo the input arguments to standard output"""  
""" EJERCICIO #1
    edad= int(input("introduce tu edad: "))
    if edad >= 18 :
        print("ERES MAYOR DE EDAD")
    else:
        print("Eres menor")"""

"""#EJERCICIO #2
 contrasena = "bochi43"
 adivina= input("ADIVINA LA CONTRASENA: ")
 if contrasena==adivina.lower():
    print("Coinciden")
 else:
    print("NO COINCIDEN")"""

"""#ejercico 3
    num1= int(input("PRIMER NUMERO: "))
    num2= int(input("PRIMER NUMERO: "))
    if num2 > 0:
        division= num1/num2
        print("EL TOTAL ES "+ str(division))
    else:
        print("SYNTAX ERROR")
    
    n = float(input("Introduce el dividendo: "))
    m = float(input("Introduce el divisior: "))
    if m == 0:
        print("¡Error! No se puede dividir por 0.")
    else:
        print(n/m)"""

"""#EJERCICIO 4
    num= int(input("INTRODUZCA UN NUMERO ENTERO: "))
    if num % 2==0 :
        print("ES PAR")
    else:
        print("NO ES PAR")"""

"""#ejercicio 5
    edad = int(input("introduce tu edad: "))
    ingresoM = float(input("Introduce tus ingresos mensuales $"))
    if ((edad>18) & (ingresoM >=1000) ):
        print("Tienes que tributar")
    else:
        print("No tienes que tributar")"""

def main():
    age = int(input("¿Cuál es tu edad? "))
    income = float(input("¿Cuales son tus ingresos mensuales?"))
    if age <= 16 or income < 1000:
        print("No tienes que cotizar")
    else:
        print("Tienes que cotizar")
    


    
 



if __name__ == '__main__':
    sys.exit(main())
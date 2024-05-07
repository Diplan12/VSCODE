
import sys
def main():
    """Echo the input arguments to standard output"""
  #  x = (input("Coloque su nombre:" "\n"))
   # n= int(input("Digite un Numero:"))
    #print ((x + "\n")* n)
   
    """ejercicio 2
    nombreC = (input("Coloque su nombre completo:" "\n"))
    mayusc = nombreC.upper()
    minyscu = nombreC.lower()
    primeraM = nombreC.title()
    print (mayusc)
    print (minyscu)
    print (primeraM)"""
    """ejercicio 3
    nombre= input("COLOQUE SU NOMBRE" "\n")
    print("Tu nombre completo "+ nombre.upper()+ " contiene " +str(len(nombre))+ " letras ")"""
    #ejercicio 4
   # numero = str(input("DIGITE SU NUMERO " ))
    #valorN=numero.split("-")
    #print(valorN[1])

    """#ejercicio 5
    frase = input("introduzca una frase: ")
    print(frase[::-1])"""

    """ejercicio 6
    frase = input("introduzca una frase: ")
    vocal = input("introduce una vocal ")
    print(frase.replace(vocal,vocal.upper()))"""""

    #ejercicio 7
    #email = input ("introduzca tu correo electronico: ")
    #usuario = email.split("@")
    #print(email[:email.find('@')] + '@ceu.es')
    #print("su correo es " + usuario[0] + "@ceu.es") 

    #ejercicio 8
    precio = str (input ("Cual es el precio ? "))
    print("$ "+ (precio[:precio.find(".")])+ " con " + (precio[precio.find('.')+1:])+ " centavos")

    """ Escribir un programa que pregunte el nombre el un producto, su precio y u
    n número de unidades y muestre por pantalla una cadena con el nombre del producto 
    seguido de su precio unitario con 6 dígitos enteros 
    y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""
    


    



  
    
   






if __name__ == '__main__':
    sys.exit(main()) 

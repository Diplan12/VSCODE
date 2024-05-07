import sys


""" palabra= input("introduzca una palabra")
    a=0
    while a<10:
        print(palabra)
        a= a+1  """

"""#ejercicio2
    num= int(input("INTRODUZCA SU EDAD: "))
    for i in range(num):
        print(f"HAS CUMPLIDO {i +1} años")"""

"""EJERCICIO 3
num= int(input("INTRODUZCA UN NUMERO POSITIVO: "))
    for i in range(num):
        print(f"NUMEROS: {i+1} {i%2 !=0}")
        if i== True:
            print("NUMERO IMPAR")
        else :
            print("NUMERO PAR")
            
    n = int(input("Introduce un número entero positivo: "))
    for i in range(1, n+1, 2):
        print(i, end=", ")"""

"""num= int(input("INTRODUZCA UN NUMERO POSITIVO: "))
    for i in range(num,-1,-1):
        print(f"valores {i}", end=", \n")"""

""" for i in range(1,11):
        print(f"{i} * 1 = {i*1}")
        print(f"{i} * 2 = {i*2}")
        print(f"{i} * 3 = {i*3}")
        print(f"{i} * 4 = {i*4}")
        print(f"{i} * 5 = {i*5}")
        print(f"{i} * 6 = {i*6}")
        print(f"{i} * 7 = {i*7}")
        print(f"{i} * 8 = {i*8}")
        print(f"{i} * 9 = {i*9}")
        print(f"{i} * 10 = {i*10}")
        print("----siguiente tabla---")

    for i in range(1,11):
        for j in range(1,11):
            print(f"{i*j}", end="\t")
        print("")"""

def main():
    #num= int(input("INTRODUZCA UN NUMERO POSITIVO: "))
  ##  for i in range(num):
    ##    for j in range(i+1):
      ##      print("*", end="")
        ##print("")
    work= input("INTRODUZCA UNA PALABRA ")
    for i in range(len(work)-1,-1,-1):
        print(work[i])

if __name__ == '__main__':
    sys.exit(main())
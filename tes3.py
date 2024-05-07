import shlex
import sys

def descuento (valor):
    desc=0.60
    total = valor *desc
    return total





def main():
    """Echo the input arguments to standard output"""
    precioBarra=3.49
    x = float(input("Barras vendidas que no son del dia:""\n"))
    print("----------------------------")
    print("El precio estandar es de : "+ str(precioBarra))
    print("El descuento aplicado será: "+ str(descuento(x)))
    print("El precio total es de : "+str((x*precioBarra)-descuento(x)))
    print("----------------------------")    
    
#test para branch
#test number 2





if __name__ == '__main__':
    sys.exit(main()) 



import math

#Ej 1
def imprimir_hola_mundo ():
    print ("Hola Mund0")

def imprimir_un_verso ():
    print ("Ay nena\nA tu cola le falta crema\nA tu boca una mamadera\nY con los piebes te la vamos a dar")

def raizDe2(): 
    return round (math.sqrt (2),4)

def factorial_de_dos () ->int :
    return math.factorial (2)

def perimetro() -> float:
    return 2*(math.pi)

#Ej 2
def imprimir_saludo (nombre:str) -> str : 
    print ("Hola "+nombre)

def raiz_cuadrada_de (numero:int) -> float :
    return math.sqrt (numero)

def fahrenheit_a_celsius (temperatura:float) -> float :
    return ((temperatura - 32 )* 5/9)

def imprimir_dos_veces(estribillo:str) -> str :
    print ((estribillo + " " )*2)

def es_multiplo_de (n,m:int) -> bool : 
    return (n%m) == 0 
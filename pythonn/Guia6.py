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

def es_par (n:int) -> bool:
    return es_multiplo_de (n,2)

def cantidad_de_pizzas (comensales,min_cant_de_porciones:int) ->int:
    return math.ceil((comensales*min_cant_de_porciones)/8)

#Ej3 
def alguno_es_0 (numero1,numero2:int)->bool:
    return (numero1 == 0) or (numero2 == 0) 

def ambos_son_0 (numero1,numero2:int)->bool:
    return (numero1==0) and (numero2==0)

def es_nombre_largo (nombre:str)->bool:
    return (len(nombre)>=3) and (len(nombre)<=8)

def es_bisiesto (año:int)->bool:
    return ((es_multiplo_de(año,4)) and (not(es_multiplo_de(año,100)))) or (año==400)

#Ej4
def peso_pino (altura:float)->float:
    res:int = 0
    if (altura < 4):
        res = altura * 100 * 3
    else : 
        res = (altura-3) *100 *2 + 900
    return res

def es_peso_util (altura:float)->bool:
    return (peso_pino(altura)>=400) and (peso_pino(altura)<=1000)

#Ej5
def devolver_si_es_par (numero:int)->bool:
    if es_par(numero)==True:
        return numero*2
    else:
        return numero
    
def lindo_nombre (nombre:str)->str:
    if len(nombre)>=5:
        print("Tu nombre tiene muchas letras")
    else:
        print ("puto el que lee")
    
        
def num_del_1_10 () :
    for i in range (1,11,1):
        print (i)

def eco ():
    for i in range(1,11):
        print("eco") 
        i+=1

def despegue (tiempo:int):
    for i in range (0,tiempo):
        print (tiempo)
        tiempo -=1
    print ("despegue")
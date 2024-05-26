import math
#Parte 1
#1.1
def pertenece (lista:list[int],num:int)-> bool:
    res:bool = False
    for i in lista:
        if (i == num):
            res = True
    return res

def pertenece2 (lista:list[int],num:int)-> bool:
    i:int = 0
    res:bool = False
    while i<len(lista):
        if (lista[i]==num):
            res = True
        i+=1
    return res

#1.2
def divide_a_todos (lista:list[int],num:int)-> bool:
   for i in lista:
       if not(i%num==0):
            return False
       return True

#1.3
def suma_total (lista:list[int])->int:
    res:int = 0
    for i in lista:
        res = res + i
    return res

#1.4      
def ordenados (lista:list[int])->bool:
    for i in range (len(lista)-1):
        if (lista[i]>lista[i+1]):
            return False
        i+=1
    return True

#1.5
def palabra_larga (lista:list[str])->bool:
    res:bool = False
    for i in lista:
        if (len(i)>7):
            res = True
            print (i)
    return res

#1.6
def capicua (palabra:str)->bool:
    u:int= (len(palabra) -1)
    for i in range(math.ceil(len(palabra)/2)):
        if not (palabra[i] == palabra[u]):
            return False
        i+=1
        u-=1
    return True

#1.7
def seguridad(contraseña:str)->str:
    res:str = "Amarillo"
    if len(contraseña) < 5:
        res = "Rojo"
    elif len(contraseña) > 8 and hay_mayusculas(contraseña) and hay_minusculas (contraseña) and hay_numeros (contraseña):
        res = "Verde"
    print (res)

def hay_minusculas (contraseñas:str)->bool:
    for i in range(len(contraseñas)):
        if (contraseñas[i] <= 'z') and (contraseñas[i] >= 'a'):
            return True
    return False

def hay_mayusculas (contraseñas:str)->bool:
    for i in range(len(contraseñas)):
        if (contraseñas[i] <= 'Z') and (contraseñas[i] >= 'A'):
            return True
    return False

def hay_numeros (contraseñas:str)->bool:
    for i in range(len(contraseñas)):
        if (contraseñas[i] <= '9' ) and (contraseñas[i] >= '0'):
            return True
    return False

#1.9
def vocales_3(palabra:str)->bool:
    vocales:list[str]=['a','e','i','o','u','A','E','I','O','U']
    n:int = 0
    for vocal in vocales:
        if vocal in palabra:
            n += 1
    return n > 2

#Parte 2
#2.1
def solo_impares (s:list[int])->list[int]:
    for i in range(len(s)):
        if (s[i]%2 == 0):
            s[i]=0
    return s

#2.2
def solo_impares2 (s:list[int])->list[int]:
    s1:list[int] = []
    for i in s:
        if (i%2 == 0):
            s1 = s1.append(0)
        else:
            s1 = s1.append(i)
    return s1

#2.3
def sin_vocales (palabra:str)->str:
    vocales:list[str]=['a','e','i','o','u','A','E','I','O','U']
    palabranueva:str = ""
    for c in palabra:
        if c not in vocales:
            palabranueva += c
    return palabranueva

#2.4
def reemplaza_vocales (s:str)->str:
    palabra:str = ""
    for c in s:
        if (es_vocal(c) == True):
            palabra += '_'
        else:
            palabra += c
    return palabra

def es_vocal (c:str)->bool:
    return (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u') or (c == 'A') or (c == 'E') or (c == 'I') or (c == 'O') or (c == 'U')

#2.5
def da_vuelta_str (s:str)->str:
    vesre:str = ""
    for c in range(0,len(s)):
        vesre+= s[(len(s)-c-1)]
    return vesre

#2.6
def eliminar_repetidos (palabra:str)->str:
    sinrep:str = "" 
    for c in palabra:
        if (sinrep.count(c) == 0):
            sinrep += c 
    return sinrep

#Ej 3
def aprobado (notas:list[int])->int:
    if notas_aprobadas(notas) == True and (promedio(notas) >=7):
        return 1
    elif notas_aprobadas(notas) == True and (promedio(notas)>=4):
        return 2 
    return 3

def notas_aprobadas (notas:list[int])->bool:
    for nota in notas:
        if (nota < 4):
            return False
    return True

def promedio (notas:list[int])->float:
    n:int = 0
    for nota in notas:
        n += nota 
    return n/len(notas)
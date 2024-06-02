from queue import LifoQueue as Pila
import numpy as np

#1.1
def contar_lineas(nombre_archivo:str)->int:
    res:int = 0
    with open (nombre_archivo,encoding='utf-8') as f:
        res = len(f.readlines())
    return res

#1.2
def existe_palabra(palabra,archivo:str)->bool:
    res:bool = False
    palabras:list[str] = (todas_palabras(archivo))
    for i in range(len(palabras)):
        if palabras[i] == palabra:
            res = True
    return res


def todas_palabras(archivo:str)->list[str]:
    res:list[str] = []
    palabra:str = ""
    with open (archivo,encoding='utf-8') as f:
        linea = f.readline()
        while linea != '':
            for i in range(len(linea)):
                if (linea[i] != ' ') and not (i == len(linea) - 1):
                    palabra += linea [i]
                else:
                    res.append(palabra)
                    palabra = ""
            linea = f.readline()
    return res

#1.3
def cantidad_de_apariciones (palabra,archivo:str)->int:
    res:int = 0
    palabras:list[str] = (todas_palabras(archivo))
    for i in range(len(palabras)):
        if palabras[i] == palabra:
            res += 1
    return res

#2
def clonar_sin_comentarios(archivo:str)->None:
    with open (archivo,encoding='utf-8') as f:
        with open ('nuevo archivo','w',encoding='utf-8') as g:
            linea = f.readline()
            while linea != '':
                if es_linea_comentada(linea) == False:
                    g.write(linea)
                linea = f.readline()

def es_linea_comentada (linea:str)->bool:
    i:int = 0
    while i <= (len(linea) -1):
        if linea[i] == '#':
            return True
        elif linea[i] == ' ':
            i +=1
        else:
            return False

with open ('nashe.txt',encoding='utf-8') as f:
    leer=f.readline()

#3
def invertir_lineas (archivo:str)->None:
    with open (archivo,encoding='utf-8') as f:
        with open ('reverso.txt','w',encoding='utf-8') as g:
            i:int = len(f.readlines())-1
            linea = f.readlines()
            while i >= 0:
                g.write(linea[i])
                i -= 1

with open ('nashe.txt',encoding='utf-8') as f:
    linea = f.readlines()
            



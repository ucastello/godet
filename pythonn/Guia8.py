import numpy as np
from queue import LifoQueue as Pila
from queue import Queue as Cola

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


def todas_palabras(archivo,token:str)->list[str]:
    res:list[str] = []
    palabra:str = ""
    with open (archivo,encoding='utf-8') as f:
        linea = f.readline()
        while linea != '':
            for i in range(len(linea)):
                if (linea[i] != token) and linea[i] != '\n':
                    palabra += linea [i]
                elif len(palabra) > 0:
                    res.append(palabra)
                    palabra = ""
            linea = f.readline()
    if len(palabra) > 0:
        res.append(palabra)
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


#3
def invertir_lineas (archivo:str)->None:
    with open (archivo,encoding='utf-8') as f:
        with open ('reverso.txt','w',encoding='utf-8') as g:
            linea = f.readlines()
            i:int = len(linea)-1
            while i >= 0:
                if (i == len(linea)-1) and (linea[i][-1] != '\n'):
                    g.write(linea[i]+'\n')
                    i-=1
                else:
                    g.write(linea[i])
                    i -= 1


#4
def agregar_frase_al_final (archivo,frase:str)->None:
    with open (archivo,'a',encoding='utf-8') as f:
        f.write('\n'+frase)

def promedio_de_estudiante (archivo,Lu:str)->float:
    suma_de_notas:float = 0
    materias:int = 0
    with open (archivo,encoding='utf-8') as f:
        linea = f.readline()
        nombre_y_promedio:tuple[str] = todas_palabras2(linea,',')[0],todas_palabras2(linea,',')[3]
        if nombre_y_promedio[0] == Lu:
            suma_de_notas += float(nombre_y_promedio[1])
            materias += 1
            linea =f.readline
        else:
            f.readline
    promedio:float = round(suma_de_notas/materias,2)
    return promedio

def todas_palabras2(linea,token:str)->list[str]:
    res:list[str] = []
    palabra:str = ""
    for letra in linea:
            if (letra != token) and (letra != '\n'):
                palabra += letra
            elif len(palabra) > 0:
                res.append(palabra)
                palabra = ""
    if len(palabra) > 0:
        res.append(palabra)
    return res

# with open ('nashe.txt',encoding='utf-8') as f:
#     leer = f.readline()
#     leerr = f.readline()
#     ler = f.readline()
#8
def generar_nros_al_azar (cantidad,desde,hasta:int)->Pila[int]:
    p:Pila[int] = Pila()
    for i in range(cantidad):
        aleatorio:int = np.random.randint(desde,hasta)
        p.put(aleatorio)
    return p 

def generar_pilas (palabras:list[str])->Pila[str]:
    p:Pila[int] = Pila()
    for palabra in range(len(palabras)):
        p.put(palabras[palabra])
    return p 

#9
def cantidad_elementos(pila:Pila[int])->int:
    pila_aux:Pila[int] = Pila()
    contador:int = 0
    while not pila.empty():
        pila_aux.put(pila.get())
        contador += 1
    devolver_a_la_pila(pila,pila_aux)
    return contador

def devolver_a_la_pila (pila_orig,pila_aux:Pila)->None:
    while not pila_aux.empty():
        pila_orig.put(pila_aux.get())

p:Pila[int] = Pila()
p.put(1)
p.put(2)

#10
def buscar_el_maximo (pila:Pila[int])->int:
    p_aux:Pila[int] = Pila()
    maximo_actual:int = pila.get()
    pila.put(maximo_actual)
    while not pila.empty:
        elem = pila.get
        if elem > maximo_actual:
            maximo_actual = elem
            p_aux.put(elem)
        else:
            p_aux.put(elem)
    devolver_a_la_pila(pila,p_aux)
    return maximo_actual

#11
def esta_bien_balancea (formula:str)->bool:
    res:bool=True
    parentesis:Pila[str]=Pila()
    for i in range (len(formula)):
        if formula[i] == '(':
            parentesis.put('(')
            if i == len(formula):
                res = False
        elif formula[i] == ')':
            if parentesis.empty():
                res = False
            else:
                parentesis.get()
    if parentesis.empty() == False:
        res = False
    return res

#12
def evaluar_expresion (formula:str)->float:
    numeros:Pila[float] = Pila()
    res:Pila[float] = Pila()
    for i in range(len(formula)):
        if formula[i] == '+':
            num1 = numeros.get()
            num2 = numeros.get()
            numeros.put(float(num2+num1))
        elif formula[i] == '-':
            num1 = numeros.get()
            num2 = numeros.get()
            numeros.put(float(num2-num1))
        elif formula[i] == '*':
            num1 = numeros.get()
            num2 = numeros.get()
            numeros.put(float(num2*num1))
        elif formula[i] == '/':
            num1 = numeros.get()
            num2 = numeros.get()
            numeros.put(float(num2/num1))
        else:
            if formula[i] != ' ':
                numeros.put(int(formula[i]))
    res.put(numeros.get())
    return res.get()

#13
def generar_nros_al_azar_cola(cantidad,desde,hasta:int)->Cola[int]:
    res:Cola[int] = Cola()
    for i in range(cantidad):
        aleatorio:int = np.random.randint(desde,hasta)
        res.put(aleatorio)
    return res

def generar_colas (cantidad:int)->Cola[int]:
    c:Cola[int] = Cola()
    n:int = 1
    for i in range(cantidad):
        c.put(n)
        n += 1
    return c

#14
def cantidad_elementos_cola(c:Cola[int])->int:
    c_aux:Cola = Cola()
    contador:int = 0 
    while not c.empty():
        c_aux.put(c.get())
        contador += 1
    mover_la_colita(c,c_aux)
    return contador

def mover_la_colita(cola_orig,cola_aux:Cola)->None:
    while not cola_aux.empty:
        cola_orig.put(cola_aux.get())

def printear_cola(cola:Cola)->list:
    lista:list = []
    while not cola.empty():
        lista.append(cola.get())
    for i in lista:
        cola.put(lista)
    return lista

#15
def buscar_el_maximo_colas(c:Cola[int])->int:
    lista_aux:list[int] = []
    lista_aux.append(c.get())
    maximo:int = lista_aux[0]
    while not c.empty():
        elem:int = c.get()
        if elem > maximo:
            maximo = elem
            lista_aux.append(elem)
        else:
            lista_aux.append(elem)
    for i in lista_aux:
        c.put(i)
    return maximo

#16
def armar_secuencia_bingo ()->Cola[int]:
    sec_bingo:Cola[int] = Cola()
    nums_disponibles:list[int] = [i for i in range(100)]
    while len(nums_disponibles) > 0:
        posicion_aleatoria:int = np.random.randint(0,len(nums_disponibles))
        sec_bingo.put(nums_disponibles[posicion_aleatoria])
        nums_disponibles.remove(nums_disponibles[posicion_aleatoria])
    return sec_bingo

def pertenece_cola (c:Cola[int],num:int)->bool:
    res:bool = False
    lista_aux:list[int] = []
    while not c.empty():
        elem = c.get()
        lista_aux.append(elem)
        if elem == num:
            res = True
    for i in lista_aux:
        c.put(i)
    return res

def pertenece (lista:list[int],num:int)-> bool:
    res:bool = False
    for i in lista:
        if (i == num):
            res = True
    return res

def jugar_carton_bingo (carton:list[int],bolillero:Cola[int])->int:
    bolas_jugadas:int = 0
    while len(carton) > 0:
        bola:int = bolillero.get()
        bolas_jugadas += 1
        if pertenece (carton,bola) == True:
            carton.remove(bola)
    return bolas_jugadas

#17
def n_pacientes_urgentes(cola:Cola[(int,str,str)])->int:
    pacientes_graves:int = 0
    lista_aux:list[(int,str,str)]
    while not cola.empty():
        paciente:tuple[int,str,str] = cola.get()
        lista_aux.append(paciente)
        if paciente[0] < 4:
            pacientes_graves += 1
    for i in lista_aux:
        cola.put(i)
    return pacientes_graves

#19
def agrupar_por_longitud (archivo:str)->dict[int,int]:
    res:dict[int,int] = dict()
    with open (archivo,encoding='utf-8') as f:
        linea = f.readline()
        while linea != '':
            palabras:list[str] = todas_palabras2(linea,' ')
            for palabra in palabras:
                longitud:int = len(palabra)
                if longitud in res.keys():
                    res[longitud] += 1
                else:
                    res[longitud] = 1
            linea = f.readline()
    return res

#20
def calcular_promedio_por_estudiante(archivo:str)->dict[str,float]:
    libreta_universitaria:dict[str,float] = dict()
    with open (archivo,encoding='utf-8') as f:
        linea = f.readline()
        while linea != '':
            if linea[0] != '\n':
                alumno:str = (todas_palabras2(linea,','))[0]
                promedio:float = promedio_estudiante(archivo,alumno)
                if alumno not in libreta_universitaria.keys():
                    libreta_universitaria[alumno] = promedio
            linea = f.readline()
    return libreta_universitaria

def promedio_estudiante (archivo,lu:str)->float:
    promedio:float = 0
    suma_notas:float = 0
    cant_materias:int = 0
    with open (archivo,encoding='utf-8') as f:
        linea = f.readline()
        while linea != '':
            if linea[0] != '\n':
                alumno_actual:str = (todas_palabras2(linea,','))[0]
                nota_actual:float = (float((todas_palabras2(linea,','))[3]))
                if (alumno_actual == lu):
                    suma_notas += nota_actual
                    cant_materias += 1
            linea = f.readline()  
    promedio = round(suma_notas / cant_materias,2)
    return promedio


#21
def la_palabra_mas_frecuente (archivo:str)->str:
    palabras_y_apariciones:dict[str,int] = dict()
    apariciones:tuple[str,int] = ("",0)
    with open (archivo,encoding='utf-8') as f:
        linea:str = f.readline()
        while linea != '':
            palabras:list[str] = todas_palabras2(linea,' ')
            for palabra in palabras:
                if palabra in palabras_y_apariciones.keys():
                    palabras_y_apariciones[palabra] += 1
                else:
                    palabras_y_apariciones[palabra] = 1
            linea = f.readline()
    for palabra in palabras_y_apariciones:
        if palabras_y_apariciones[palabra] > apariciones[1]:
            apariciones = (palabra,palabras_y_apariciones[palabra])
    return apariciones[0]

#22
def visitar_sitio (historiales:dict[str,Pila[str]],usuario,sitio:str)->None:
    for usuarios in historiales.keys():
        if usuarios == usuario:
            historiales[usuario].put(sitio)
    return historiales


#Parcial 1
def ind_nesima_aparicion (lista:list[int],n,elem:int)->int:
    res:int = -1
    for i in range(len(lista)):
        if lista[i] == elem:
            n -= 1
            if n == 0:
                res = i
    return res 

def mezclar (s1,s2:list[int])-> list[int]:
    res:list[int] = []
    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])
    return res

def frecuencia_posiciones_por_caballo (caballos:list[str],resultados:dict[str,list[str]])->dict[str,list[int]]:
    res:dict[str,list[int]] = dict()
    posiciones = resultados.values()
    posicion:int = 0
    for caballo in caballos:
        res[caballo] = [0]*len(caballos)
        for carrera in posiciones:
            for j in carrera:
                if j == caballo:
                    res[caballo][posicion] += 1
                else:
                    posicion +=1
            posicion = 0
    return res 

def matriz_capicua (matriz:list[list[int]])->bool:
    res:bool = True
    j = len(matriz[0]) -1
    for filas in matriz:
        for i in range(int(len(filas)/2)):
            if filas[i] != filas[j-i]:
                res = False
    return res

#Parcial2
#1
def hay_una_recarga (historial:str) ->bool:
    res:bool = True
    i:int = 0
    while historial[i] != 'x':
        if historial[i] == 's':
            i += 1
        elif historial[i] != 'r':
            return False
        else:
            return True
        
def verificar_transacciones (historial:str)->int:
    saldo:int = 0
    i:int = 0
    if hay_una_recarga(historial) == True:
        while saldo >= 0 and historial[i] != 'x':    
            if historial[i] == 'r':
                saldo += 350
            elif historial[i] == 'v':
                saldo -= 56 
            i += 1
    if saldo < 0 :
        saldo += 56
    return saldo

#2
def valor_minimo(temperaturas:list[tuple[float,float]])->float:
    minimo:float = temperaturas[0][0]
    for maxima_minima in temperaturas:
        minima:float = maxima_minima[0]
        if minima < minimo :
            minimo = minima
    return minimo

#3   
def valores_extremos (cotizaciones_diarias:dict[str,list[tuple[int,float]]])->dict[str,tuple[float,float]]:
    res:dict[str,tuple[float,float]] = dict()
    for empresa in cotizaciones_diarias.keys():
        res[empresa] = (es_extremo(cotizaciones_diarias[empresa],1),es_extremo(cotizaciones_diarias[empresa],(-1)))
    return res

def es_extremo(cotizaciones:list[tuple[int,float]],indicador:int)->float:
    extremo:float = indicador*cotizaciones[0][1]
    for cotizacion in cotizaciones:
        valor:float = indicador*cotizacion[1]
        if valor < extremo :
            extremo = valor
    extremo *= indicador
    return extremo

#4
def hay_repetidos(nums:list[int],n)->bool:
    res:bool = False
    repeticiones:int = 0
    for num in nums:
        if num == n:
            repeticiones += 1
    if repeticiones > 1:
        res = True
    if n == 0:
        res = False
    return res

def es_sudoku_valido(tablero:list[list[int]])->bool:
    res:bool = True
    columnas:list[list[int]] = armar_columna(tablero)
    for filas in tablero:
        for cuadrante in filas:
            if hay_repetidos(filas,cuadrante) == True:
                res = False
    for columna in columnas:
        for cuadrante in columna:
            if hay_repetidos(columna,cuadrante) == True:
                res = False
    return res

def armar_columna (tablero:list[list[int]])->list[int]:
    res:list[list[int]] = []
    todos:list[int] = []
    columna_actual:list[int] = []
    for i in tablero:
        for numeros in i:
            todos.append(numeros)
    for columnas in range(9):
        for i in range(len(todos)):
            if i%9 == columnas%9:
                columna_actual.append(todos[i])
        res.append(columna_actual)
        columna_actual = []
    return res

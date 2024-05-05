module Unparcial where 
------------------- ej 1 -------------------
atajaronSuplentes :: [(String,String)] -> [Integer] -> Integer -> Integer
atajaronSuplentes (x:xs) (y:ys) n = n - golesTitulares (x:xs) (y:ys)

golesTitulares :: [(String,String)] -> [Integer] -> Integer
golesTitulares [x] [y] = y
golesTitulares (x:xs) (y:ys) = y + golesTitulares xs ys

------------------- ej 2 -------------------
-- equiposValidos :: [(String,String)] -> Bool
-- equiposValidos [] = True
-- equiposValidos (x:xs) = sePuedenAnotar (x:xs) && equiposValidos xs

-- sePuedenAnotar :: [(String,String)] -> Bool
-- sePuedenAnotar [] = True
-- sePuedenAnotar [(x,y)] = x/=y
-- sePuedenAnotar ((x,y):(n,m):xs) | x/=n && x/=m && y/=n && y/=m && sePuedenAnotar ((x,y):xs) = True
--                                 | otherwise = False

------------------- ej 3 -------------------
-- porcentajeDeGoles :: String -> [(String,String)] -> [Integer] -> Float
-- porcentajeDeGoles n xs ys = division (golesAlArquero n xs ys) (golesTitulares xs ys) *100

-- division :: Integer -> Integer -> Float
-- division a b = fromIntegral a / fromIntegral b

-- golesAlArquero :: String -> [(String,String)] -> [Integer] -> Integer
-- golesAlArquero n [x] [g] = g
-- golesAlArquero n ((x,y):xs) (g:gs) | n == y = g
--                                    | otherwise = golesAlArquero n xs gs

------------------- ej 4 -------------------
vallaMenosVencida :: [(String,String)] -> [Integer] -> String
vallaMenosVencida xs gs = fst (minimo (golesACadaArquero (xs) gs))

golesACadaArquero :: [(String,String)] -> [Integer] -> [(String,Integer)]
golesACadaArquero [(x,y)] [g] = [(y,g)]
golesACadaArquero ((x,y):xs) (g:gs) = (y,g) : golesACadaArquero xs gs

minimo :: [(String,Integer)] -> (String,Integer)
minimo [x] = x
minimo ((x,g):(x1,g1):xs) | g <= g1 = minimo ((x,g):xs)
                          | otherwise = minimo ((x1,g1):xs)

------------------------------------------------------------ Otro Parcial------------------------------------------------------------
------------------- ej 1 -------------------
golesDeNoGoleadores :: [(String,String)] -> [Integer] -> Integer -> Integer
golesDeNoGoleadores (x:xs) (g:gs) total = total - golesDeGoleadores (x:xs) (g:gs)

golesDeGoleadores :: [(String,String)] -> [Integer] -> Integer
golesDeGoleadores [] [] = 0
golesDeGoleadores (x:xs) (g:gs) = g + golesDeGoleadores xs gs

------------------- ej 2 -------------------
equiposValidos :: [(String,String)] -> Bool
equiposValidos [] = True
equiposValidos (x:xs) = soyGladys (x:xs) && equiposValidos xs

soyGladys :: [(String,String)] -> Bool
soyGladys [] = True
soyGladys [(x,y)] = x/=y
soyGladys ((x,y):(x1,y1):xs) | x/=x1 && x/=y1 && y/= x1 && y/=y1 && soyGladys ((x,y):xs) = True
                             | otherwise = False

------------------- ej 3 -------------------
porcentajeDeGoles :: String -> [(String,String)] -> [Integer] -> Float
porcentajeDeGoles "" [] [] = 0
porcentajeDeGoles n (x:xs) (g:gs) = division (golesDelGoleador n (x:xs) (g:gs)) (golesDeGoleadores (x:xs)(g:gs)) *100

golesDelGoleador :: String -> [(String,String)] -> [Integer] -> Integer
golesDelGoleador _ [x] [g] = g
golesDelGoleador n ((x,y):xs) (g:gs) | n == y = g
                                     | otherwise = golesDelGoleador n xs gs

division :: Integer -> Integer -> Float
division a b = fromIntegral a / fromIntegral b 

------------------- ej 4 -------------------
botinDeOro :: [(String,String)] -> [Integer] -> String
botinDeOro [] [] = []
botinDeOro (x:xs) (g:gs) = fst (maximo (golesGoleador (x:xs)(g:gs)))

golesGoleador :: [(String,String)] -> [Integer] -> [(String,Integer)]
golesGoleador [(x,y)] [g] = [(y,g)]
golesGoleador ((x,y):xs) (g:gs) = (y,g) : golesGoleador xs gs

maximo :: [(String,Integer)] -> (String,Integer)
maximo [(y,g)] = (y,g)
maximo ((y,g):(y1,g1):xs) | g >= g1 = maximo ((y,g):xs)
                          | otherwise = maximo ((y1,g1):xs)

------------------------------------------------------------ Otro Parcial------------------------------------------------------------
------------------- ej 1 -------------------
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((a,b):xs) = laTuplaEstaPermitida ((a,b):xs) && relacionesValidas xs

laTuplaEstaPermitida :: [(String,String)] -> Bool
laTuplaEstaPermitida [] = True  
laTuplaEstaPermitida [(a,b)] = a/=b 
laTuplaEstaPermitida ((a,b):(c,d):xs) = (a,b) /= (c,d) && (b,a) /= (c,d) && laTuplaEstaPermitida ((a,b):xs) 

------------------- ej 2 -------------------
personas :: [(String,String)] -> [String]
personas [] = []
personas (x:xs) = sacarRepetido (personasRepetidas (x:xs))

personasRepetidas :: [(String,String)] -> [String]
personasRepetidas [] = []
personasRepetidas ((x,y):xs) = x : y : personasRepetidas xs

sacarPersona :: String -> [String] -> [String]
sacarPersona _ [] = []
sacarPersona p (x:xs) | p == x = sacarPersona p xs 
                      | otherwise = x : sacarPersona p xs 

sacarRepetido :: [String] -> [String]
sacarRepetido [] = []
sacarRepetido (x:xs) = x : sacarPersona x (sacarRepetido xs)

------------------- ej 3 -------------------
amigosDe :: String -> [(String,String)] -> [String]
amigosDe p (x:xs) = sacarPersona p (personasRepetidas (amiguisdeP p (x:xs)))

amiguisdeP :: String -> [(String,String)] -> [(String,String)]
amiguisdeP _ [] = []
amiguisdeP p ((x,y):xs) | p == x || p == y = (x,y) : amiguisdeP p xs   
                        | otherwise = amiguisdeP p xs

------------------- ej 4 -------------------
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos [] = []
personaConMasAmigos (x:xs) = maximodeaca (personasYsusAmigos (personas (x:xs)) (x:xs))

cuantasVecesAparece :: String -> [(String,String)] -> Integer
cuantasVecesAparece _ [] = 0
cuantasVecesAparece n ((x,y):xs) | n == x || n == y = 1 + cuantasVecesAparece n xs
                                 | otherwise = cuantasVecesAparece n xs 

personasYsusAmigos :: [String] -> [(String,String)] -> [(String,Integer)]
personasYsusAmigos [] _ = []
personasYsusAmigos (p:ps) (x:xs) = (p,cuantasVecesAparece p (x:xs)) : personasYsusAmigos ps (x:xs)

maximodeaca :: [(String,Integer)] -> String 
maximodeaca [(p,a)] = p 
maximodeaca ((p,a):(p1,a1):xs) | a >= a1 = maximodeaca ((p,a):xs)
                               | otherwise = maximodeaca ((p1,a1):xs)
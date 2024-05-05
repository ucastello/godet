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
porcentajeDeGoles n (x:xs) (g:gs) = division (golesDelGoleador n (x:xs) (g:gs)) (golesDeGoleadores (x:xs)(g:gs))

golesDelGoleador :: String -> [(String,String)] -> [Integer] -> Integer
golesDelGoleador _ [x] [g] = g
golesDelGoleador n ((x,y):xs) (g:gs) | n == y = g
                                     | otherwise = golesDelGoleador n xs gs

division :: Integer -> Integer -> Float
division a b = fromIntegral a / fromIntegral b 

------------------- ej 4 -------------------
botinDeOro :: [(String,String)] -> [Integer] -> String
botinDeOro (x:xs) (g:gs) = fst (maximo (golesGoleador (x:xs)(g:gs)))

golesGoleador :: [(String,String)] -> [Integer] -> [(String,Integer)]
golesGoleador [(x,y)] [g] = [(y,g)]
golesGoleador ((x,y):xs) (g:gs) = (y,g) : golesGoleador xs gs

maximo :: [(String,Integer)] -> (String,Integer)
maximo [(y,g)] = (y,g)
maximo ((y,g):(y1,g1):xs) | g >= g1 = maximo ((y,g):xs)
                          | otherwise = maximo ((y1,g1):xs)

------------------- ej 1 -------------------
atajaronSuplentes :: [(String,String)] -> [Integer] -> Integer -> Integer 
atajaronSuplentes (x:xs) (y:ys) n = n - golesTitulares (x:xs) (y:ys)

golesTitulares :: [(String,String)] -> [Integer] -> Integer
golesTitulares [x] [y] = y
golesTitulares (x:xs) (y:ys) = y + golesTitulares xs ys

------------------- ej 2 -------------------
equiposValidos :: [(String,String)] -> Bool
equiposValidos [] = True
equiposValidos (x:xs) = sePuedenAnotar (x:xs) && equiposValidos xs

sePuedenAnotar :: [(String,String)] -> Bool
sePuedenAnotar [] = True
sePuedenAnotar [(x,y)] = x/=y 
sePuedenAnotar ((x,y):(n,m):xs) | x/=n && x/=m && y/=n && y/=m && sePuedenAnotar ((x,y):xs) = True
                                | otherwise = False

------------------- ej 3 -------------------
porcentajeDeGoles :: String -> [(String,String)] -> [Integer] -> Float
porcentajeDeGoles n xs ys = division (golesAlArquero n xs ys) (golesTitulares xs ys) *100

division :: Integer -> Integer -> Float
division a b = fromIntegral a / fromIntegral b

golesAlArquero :: String -> [(String,String)] -> [Integer] -> Integer
golesAlArquero n [x] [g] = g
golesAlArquero n ((x,y):xs) (g:gs) | n == y = g
                                   | otherwise = golesAlArquero n xs gs

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
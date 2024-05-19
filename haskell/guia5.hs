-------------- Practica 5 ------------------

--------------ej 1------------------
--a
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
--b
ultimo :: [t] -> t
ultimo (x:[]) = x 
ultimo (x:xs) = ultimo (xs)
--c
principio :: [t] -> [t]
principio (x:[]) = []
principio (x:xs) = x : principio xs
--d
reverso :: [t] -> [t]
reverso (x:[]) = [x]
reverso [] = []
reverso (x:xs) = ultimo xs : reverso (principio (x:xs)) 

--------------ej 2------------------

--a
pertenece :: (Eq t) => t-> [t]->Bool
pertenece n [] = False
pertenece n (x:xs) = n == x || pertenece n (xs) 
--b
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:[]) = True
todosIguales (x:xs) = x == (head xs) && todosIguales xs
--c
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | pertenece x (xs) == True = False
                      | otherwise = todosDistintos xs 
--d
hayRepetidos :: (Eq t) =>[t]->Bool
hayRepetidos [] = False
hayRepetidos [_] = False
hayRepetidos (x:xs) | pertenece (head (x:xs)) (x:xs) == True && pertenece (head (x:xs)) (xs) == True = True
                    | otherwise = hayRepetidos (xs)
--e               
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | n /= x = x : (quitar n (xs))
--f
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs
--g
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos (x:xs) | hayRepetidos (x:xs) == False = (x:xs)
                         | otherwise = x : quitarTodos x (eliminarRepetidos xs)
--h
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x:xs) (y:ys) = conjuntoPertenece (x:xs) (y:ys) && conjuntoPertenece (y:ys) (x:xs)

conjuntoPertenece :: (Eq t) => [t] -> [t] -> Bool
conjuntoPertenece [] _ = True
conjuntoPertenece (x:xs) (y:ys) | otherwise = pertenece x (y:ys) && conjuntoPertenece xs (y:ys)

longitudReal :: (Eq t) => [t] -> Integer
longitudReal (x:xs) = longitud (eliminarRepetidos (x:xs))
--i
capicua :: (Eq t) => [t] -> Bool
capicua (x:xs) = (x:xs) == reverso (x:xs)

--------------ej 3------------------

--a
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs
--b
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs
--c
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
              | otherwise = maximo (y:xs)
--d
sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = n+x : sumarN n xs
--e
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN x (x:xs)
--f
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)
--g
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | esPar x == True = x : pares xs
             | otherwise = pares xs

esPar :: Integer -> Bool
esPar x = mod x 2 == 0
--h
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | esMultiplodeN n x == True = x : multiplosDeN n (xs)
                      | otherwise = multiplosDeN n (xs)

esMultiplodeN :: Integer -> Integer -> Bool
esMultiplodeN n m = mod m n == 0
--i
ordenar :: [Integer] -> [Integer]
ordenar (x:xs) = reverso (ordenarAux (x:xs))

ordenarAux :: [Integer] -> [Integer]
ordenarAux [] = []
ordenarAux (x:xs) = maximo (x:xs) : ordenarAux (quitar (maximo (x:xs)) (x:xs))

--------------ej 3------------------

--a
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == y && x== ' ' = sacarBlancosRepetidos (x:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs)
--b
contarPalabras :: [Char] -> Integer
contarPalabras (x:xs) = contarEspacios (palabraBienEscrita (x:xs)) + 1

sacarEspaciosAlPrincipio :: [Char] -> [Char]
sacarEspaciosAlPrincipio [] = []
sacarEspaciosAlPrincipio (x:xs) | x /= ' ' = (x:xs)
                                | x == ' ' = sacarEspaciosAlPrincipio xs


sacarEspaciosAlFinal :: [Char] -> [Char]
sacarEspaciosAlFinal xs = reverso (sacarEspaciosAlPrincipio (reverso xs))

palabraBienEscrita :: [Char] -> [Char]
palabraBienEscrita [] = []
palabraBienEscrita (x:xs) = (sacarBlancosRepetidos (sacarEspaciosAlFinal (sacarEspaciosAlPrincipio (x:xs))))

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x == ' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs
--c
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) = primeraPalabra (palabraBienEscrita (x:xs)) : palabras (sacarPrimeraPalabra (palabraBienEscrita (x:xs)))

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x:xs) | x == ' ' = []
                      | otherwise = x : primeraPalabra xs

sacarPrimeraPalabra :: [Char] -> [Char]
sacarPrimeraPalabra [] = []
sacarPrimeraPalabra (x:xs) | x== ' ' = xs
                           | otherwise = sacarPrimeraPalabra xs
--d
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs
--e
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ [' '] ++ aplanarConBlancos xs
--f
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ (nBlancos n) ++ aplanarConNBlancos xs n

nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos x = ' ' : nBlancos (x-1)
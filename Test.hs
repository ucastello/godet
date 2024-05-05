import Unparcial
import Test.HUnit

testgolesDeNoGoleadores = test [
                        "No hay goleadores de no goleadores" ~: golesDeNoGoleadores [("a","b"),("c","d")] [1,3] 4 ~?= 0,
                        "No hubo goles" ~: golesDeNoGoleadores [("a","b"),("c","d")] [0,0] 0 ~?= 0,
                        "Metieron goles" ~: golesDeNoGoleadores [("a","b"),("c","d")] [1,3] 8 ~?= 4
                        ]

testequiposValidos = test [
                   "Nadie se anoto che" ~: equiposValidos [] ~?= True,
                   "Se anoto uno solo che" ~: equiposValidos [("a","b")] ~?= True,
                   "se anotaron dos veces" ~: equiposValidos [("a","b"),("c","d"),("c","d")] ~?= False,
                   "Tienen el mismo nombre" ~: equiposValidos [("a","b"),("c","d"),("c","g")] ~?= False,
                   "Le esta haciendo burla" ~: equiposValidos [("a","b"),("c","d"),("d","g")] ~?= False
                    ]

testporcentajeDeGoles = test [
                      "Ya te dije que no vino nadie" ~: porcentajeDeGoles "" [] [] ~?= 0,
                      "Amigo cayo haaland" ~: porcentajeDeGoles "Haaland" [("city","Haaland"),("bosta","gagani")] [10,0] ~?= 100,
                      "Amigo cayo cavani" ~: porcentajeDeGoles "gagani" [("city","Haaland"),("bosta","gagani")] [10,0] ~?= 0
                      ]

testbotinDeOro = test [
               "Somos unos fracasados" ~: botinDeOro [] [] ~?= [],
               "Nadie metio goles nene" ~: botinDeOro [("a","b"),("c","d"),("c","d")] [0,0,0] ~?= "b",
               "Haaland estaba" ~: botinDeOro [("city","Haaland"),("bosta","gagani"),("psg","mbappe")] [10,0,9] ~?= "Haaland"
                ]
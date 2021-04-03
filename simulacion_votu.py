import random
from random import sample
votos = {"voto_accion" : 0,
    "voto_alianza" : 0,
    "voto_avanza" : 0,
    "voto_fuerza" : 0,
    "voto_juntos" : 0,
    "voto_partido" : 0,
    "voto_podemos" : 0,
    "voto_renovacion" : 0,
    "voto_somos" : 0,
    "voto_victoria" : 0}

voto_totales = 0

class Votante:
    def __init__(self):
        self.indice_voto = {
        "accion" : 0,
        "alianza" : 0,
        "avanza" : 0,
        "fuerza" : 0,
        "juntos" : 0,
        "partido" : 0,
        "podemos" : 0,
        "renovacion" : 0,
        "somos" : 0,
        "victoria" : 0}
        self.tematicas = [1,2,3,4,5,6,7,8]

    def elegir_tematicas(self,numero_tematicas):
        tematicas_elegidas = sample(self.tematicas,numero_tematicas)
        temas = {
            1:self.opcion_salud,
            2:self.opcion_educacion,
            3:self.opcion_crecimiento,
            4:self.opcion_impuestos,
            5:self.opcion_seguridad,
            6:self.opcion_gobernabilidad,
            7:self.opcion_derechos,
            8:self.opcion_medio,
        }
        for i in tematicas_elegidas:
            # print(f'Mi tematica es {i}')
            temas[i]()
        # print(f'Terminé de Responder la encuesta, ahora decidiré mi voto')
    
    def opcion_salud(self):
        sal1= [1,2,3,4,5]
        sal2= [1,2,3,4,5]
        sal3= [1,2,3,4,5]
        sal4= [1,2,3,4]
        respuesta1 = random.choice(sal1)
        respuesta2 = random.choice(sal2)
        respuesta3 = random.choice(sal3)
        respuesta4 = random.choice(sal4)
        if respuesta1 == 1:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta1 == 2:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta1 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["somos"] += 1  
        if respuesta1 == 4:
            self.indice_voto["accion"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta1 == 5:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1

        if respuesta2 == 1:
            self.indice_voto["avanza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta2 == 2:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
        if respuesta2 == 3:
            self.indice_voto["partido"] += 1
        if respuesta2 == 4:
            self.indice_voto["fuerza"] += 1
        if respuesta2 == 5:
            self.indice_voto["accion"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta3 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta3 == 2:
            self.indice_voto["renovacion"] += 1
        if respuesta3 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta3 == 4:
            self.indice_voto["partido"] += 1
        if respuesta3 == 5:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1

        if respuesta4 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
        if respuesta4 == 2:
            self.indice_voto["accion"] += 1
            self.indice_voto["juntos"] += 1
        if respuesta4 == 3:
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta4 == 4:
            self.indice_voto["accion"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1  
        # print(f'Respondí la encuesta de Salud')

    def opcion_educacion(self):
        edu1= [1,2,3,4,5]
        edu2= [1,2,3,4]
        edu3= [1,2,3,4,5]
        edu4= [1,2,3,4]
        edu5= [1,2,3,4,5]
        edu6= [1,2,3]
        edu7= [1,2,3]
        respuesta1 = random.choice(edu1)
        respuesta2 = random.choice(edu2)
        respuesta3 = random.choice(edu3)
        respuesta4 = random.choice(edu4)
        respuesta5 = random.choice(edu5)
        respuesta6 = random.choice(edu6)
        respuesta7 = random.choice(edu7)
        if respuesta1 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["podemos"] += 1
        if respuesta1 == 2:
            self.indice_voto["fuerza"] += 1
        if respuesta1 == 3:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta1 == 4:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1  
            self.indice_voto["somos"] += 1  
        if respuesta1 == 5:
            self.indice_voto["alianza"] += 1 

        if respuesta2 == 1:
            self.indice_voto["accion"] += 1
            self.indice_voto["podemos"] += 1
        if respuesta2 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta2 == 3:
            self.indice_voto["victoria"] += 1
        if respuesta2 == 4:
            self.indice_voto["juntos"] += 1


        if respuesta3 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
        if respuesta3 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta3 == 3:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta3 == 4:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta3 == 5:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1

        if respuesta4 == 1:
            self.indice_voto["accion"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta4 == 2:
            self.indice_voto["accion"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta4 == 3:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
        if respuesta4 == 4:
            self.indice_voto["accion"] += 1
            self.indice_voto["podemos"] += 1

        if respuesta5 == 1:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
        if respuesta5 == 2:
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta5 == 3:
            self.indice_voto["victoria"] += 1
        if respuesta5 == 4:
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta5 == 5:
            self.indice_voto["avanza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1

        if respuesta6 == 1:
            self.indice_voto["avanza"] += 1
            self.indice_voto["juntos"] += 1
        if respuesta6 == 2:
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta6 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta7 == 1:
            self.indice_voto["juntos"] += 1
        if respuesta7 == 2:
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
        if respuesta7 == 3:
            self.indice_voto["victoria"] += 1
        # print(f'Respondí la encuesta de Educacion')

    def opcion_crecimiento(self):
        cre1= [1,2,3,4,5]
        cre2= [1,2,3]
        cre3= [1,2,3,4,5]
        cre4= [1,2,3,4,5]
        respuesta1 = random.choice(cre1)
        respuesta2 = random.choice(cre2)
        respuesta3 = random.choice(cre3)
        respuesta4 = random.choice(cre4)
        if respuesta1 == 1:
            self.indice_voto["accion"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta1 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["avanza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["somos"] += 1  
        if respuesta1 == 3:
            self.indice_voto["somos"] += 1  
        if respuesta1 == 4:
            self.indice_voto["podemos"] += 1
        if respuesta1 == 5:
            self.indice_voto["juntos"] += 1

        if respuesta2 == 1:
            self.indice_voto["avanza"] += 1
            self.indice_voto["fuerza"] += 1
        if respuesta2 == 2:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta2 == 3:
            self.indice_voto["podemos"] += 1

        if respuesta3 == 1:
            self.indice_voto["somos"] += 1
        if respuesta3 == 2:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
        if respuesta3 == 3:
            self.indice_voto["alianza"] += 1
            self.indice_voto["podemos"] += 1  
            self.indice_voto["victoria"] += 1
        if respuesta3 == 4:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
        if respuesta3 == 5:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1

        if respuesta4 == 1:
            self.indice_voto["accion"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta4 == 2:
            self.indice_voto["juntos"] += 1
        if respuesta4 == 3:
            self.indice_voto["alianza"] += 1
            self.indice_voto["partido"] += 1 
            self.indice_voto["victoria"] += 1 
        if respuesta4 == 4:
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta4 == 5:
            self.indice_voto["partido"] += 1
            self.indice_voto["victoria"] += 1
        # print(f'Respondí la encuesta de Crecimiento')

    def opcion_impuestos(self):
        imp1= [1,2,3,4,5]
        imp2= [1,2,3,4,5]
        imp3= [1,2,3,4,5]
        respuesta1 = random.choice(imp1)
        respuesta2 = random.choice(imp2)
        respuesta3 = random.choice(imp3)
        if respuesta1 == 1:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta1 == 2:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
        if respuesta1 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1 
            self.indice_voto["podemos"] += 1 
        if respuesta1 == 4:
            self.indice_voto["accion"] += 1
            self.indice_voto["juntos"] += 1
        if respuesta1 == 5:
            self.indice_voto["avanza"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta2 == 1:
            self.indice_voto["juntos"] += 1
        if respuesta2 == 2:
            self.indice_voto["accion"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta2 == 3:
            self.indice_voto["avanza"] += 1
        if respuesta2 == 4:
            self.indice_voto["avanza"] += 1
            self.indice_voto["juntos"] += 1
        if respuesta2 == 5:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["avanza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta3 == 1:
            self.indice_voto["accion"] += 1
            self.indice_voto["fuerza"] += 1
        if respuesta3 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta3 == 3:
            self.indice_voto["avanza"] += 1
        if respuesta3 == 4:
            self.indice_voto["accion"] += 1
        if respuesta3 == 5:
            self.indice_voto["alianza"] += 1

        # print(f'Respondo la encuesta de Impuestos')


    def opcion_seguridad(self):
        seg1= [1,2,3,4,5]
        seg2= [1,2,3,4,5]
        seg3= [1,2,3]
        seg4= [1,2,3,4,5]
        respuesta1 = random.choice(seg1)
        respuesta2 = random.choice(seg2)
        respuesta3 = random.choice(seg3)
        respuesta4 = random.choice(seg4)
        if respuesta1 == 1:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta1 == 2:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["avanza"] += 1 
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1 
            self.indice_voto["somos"] += 1
        if respuesta1 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["fuerza"] += 1 
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1 
            self.indice_voto["victoria"] += 1
        if respuesta1 == 4:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1 
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["somos"] += 1 
        if respuesta1 == 5:
            self.indice_voto["alianza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1

        if respuesta2 == 1:
            self.indice_voto["partido"] += 1
        if respuesta2 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
        if respuesta2 == 3:
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1
        if respuesta2 == 4:
            self.indice_voto["juntos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta2 == 5:
            self.indice_voto["victoria"] += 1


        if respuesta3 == 1:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
        if respuesta3 == 2:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
        if respuesta3 == 3:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1  
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta4 == 1:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
        if respuesta4 == 2:
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
        if respuesta4 == 3:
            self.indice_voto["accion"] += 1
        if respuesta4 == 4:
            self.indice_voto["alianza"] += 1
            self.indice_voto["somos"] += 1
        if respuesta4 == 5:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1 
        # print(f'Respondo la encuesta de Seguridad')
        

    def opcion_gobernabilidad(self):
        gob1= [1,2,3]
        gob2= [1,2,3,4,5]
        gob3= [1,2,3,4]
        respuesta1 = random.choice(gob1)
        respuesta2 = random.choice(gob2)
        respuesta3 = random.choice(gob3)
        if respuesta1 == 1:
            self.indice_voto["accion"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta1 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1  
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta1 == 3:
            self.indice_voto["avanza"] += 1

        if respuesta2 == 1:
            self.indice_voto["victoria"] += 1
        if respuesta2 == 2:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1    
        if respuesta2 == 3:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1  
        if respuesta2 == 4:
            self.indice_voto["accion"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1  
        if respuesta2 == 5:
            self.indice_voto["avanza"] += 1

        if respuesta3 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta3 == 2:
            self.indice_voto["avanza"] += 1
        if respuesta3 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1  
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1
        if respuesta3 == 4:
            self.indice_voto["renovacion"] += 1
        # print(f'Respondo la encuesta de Gobernabilidad')

    def opcion_derechos(self):
        der1= [1,2,3,4,5]
        der2= [1,2,3,4,5]
        der3= [1,2,3]
        der4= [1,2,3,4,5]
        der5= [1,2,3]
       
        respuesta1 = random.choice(der1)
        respuesta2 = random.choice(der2)
        respuesta3 = random.choice(der3)
        respuesta4 = random.choice(der4)
        respuesta5 = random.choice(der5)
    
        if respuesta1 == 1:
            self.indice_voto["alianza"] += 1
            self.indice_voto["juntos"] += 1
        if respuesta1 == 2:
            self.indice_voto["partido"] += 1
        if respuesta1 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["juntos"] += 1  
        if respuesta1 == 4:
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1  
        if respuesta1 == 5:
            self.indice_voto["fuerza"] += 1 
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1


        if respuesta2 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta2 == 2:
            self.indice_voto["juntos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta2 == 3:
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta2 == 4:
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
        if respuesta2 == 5:
            self.indice_voto["alianza"] += 1
            self.indice_voto["avanza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["victoria"] += 1


        if respuesta3 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
        if respuesta3 == 2:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["avanza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta4 == 1:
            self.indice_voto["alianza"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["renovacion"] += 1
        if respuesta4 == 2:
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
        if respuesta4 == 3:
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta4 == 4:
            self.indice_voto["accion"] += 1
        if respuesta4 == 5:
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1

        if respuesta5 == 1:
            self.indice_voto["juntos"] += 1
        if respuesta5 == 2:
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta5 == 3:
            self.indice_voto["accion"] += 1
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["somos"] += 1
        # print(f'Respondo la encuesta de Derechos')

    def opcion_medio(self):
        med1= [1,2,3]
        med2= [1,2,3,4]
        med3= [1,2,3,4]
        med4= [1,2,3]
        respuesta1 = random.choice(med1)
        respuesta2 = random.choice(med2)
        respuesta3 = random.choice(med3)
        respuesta4 = random.choice(med4)
        if respuesta1 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta1 == 2:
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1  
        if respuesta1 == 3:
            self.indice_voto["alianza"] += 1
            self.indice_voto["juntos"] += 1  
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
            self.indice_voto["victoria"] += 1

        if respuesta2 == 1:
            self.indice_voto["juntos"] += 1
        if respuesta2 == 2:
            self.indice_voto["renovacion"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta2 == 3:
            self.indice_voto["alianza"] += 1
            self.indice_voto["fuerza"] += 1
        if respuesta2 == 4:
            self.indice_voto["partido"] += 1

        if respuesta3 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta3 == 2:
            self.indice_voto["fuerza"] += 1
        if respuesta3 == 3:
            self.indice_voto["partido"] += 1
            self.indice_voto["somos"] += 1  
        if respuesta3 == 4:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["podemos"] += 1

        if respuesta4 == 1:
            self.indice_voto["juntos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta4 == 2:
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["podemos"] += 1
            self.indice_voto["somos"] += 1
            self.indice_voto["victoria"] += 1
        if respuesta4 == 3:
            self.indice_voto["avanza"] += 1
            self.indice_voto["fuerza"] += 1
            self.indice_voto["juntos"] += 1
            self.indice_voto["partido"] += 1
            self.indice_voto["renovacion"] += 1
        # print(f'Respondo la encuesta de Medio Ambiente')

    def voto_final(self):
        global voto_totales,votos
        voto_totales = voto_totales + 1
        indice_mas_alto = 0
        partidos_indice_mas_alto = {}
        for i in self.indice_voto.items():
            if i[1] >= indice_mas_alto: 
                indice_mas_alto = i[1]
        for i in self.indice_voto.items():
            if i[1] == indice_mas_alto:
                partidos_indice_mas_alto[i[0]]= indice_mas_alto
        
        voto_final = random.choice(list(partidos_indice_mas_alto))

        # print(f'Mis indices mas altos son {partidos_indice_mas_alto}')
        if voto_final == "accion": votos["voto_accion"] += 1
        if voto_final == "alianza": votos["voto_alianza"] += 1
        if voto_final == "avanza":votos[ "voto_avanza"] += 1
        if voto_final == "fuerza": votos["voto_fuerza"] += 1
        if voto_final == "juntos": votos["voto_juntos"] += 1
        if voto_final == "partido": votos["voto_partido"] += 1
        if voto_final == "podemos": votos["voto_podemos"] += 1
        if voto_final == "renovacion": votos["voto_renovacion"] += 1
        if voto_final == "somos": votos["voto_somos"] += 1
        if voto_final == "victoria": votos["voto_victoria"] += 1
        # print(f'He votado por {voto_final}')

def votacion(numero_votantes):
    for i in range(numero_votantes):
        votante = Votante()
        # votante.opcion_crecimiento()
        votante.elegir_tematicas(3)
        votante.voto_final()
    print("Se realizaron las votaciones")
    print("Preparando los resultados")
    resultado()

def  resultado():
    print(votos)
    resultados = list(votos.items())
    
    print(f'Acción popular tiene: {porcentaje(resultados[0])}')
    print(f'Alianza para el Progreso tiene: {porcentaje(resultados[1])}')
    print(f'Avanza País tiene: {porcentaje(resultados[2])}')
    print(f'Fuerza Popular tiene: {porcentaje(resultados[3])}')
    print(f'Juntos por el Perú tiene: {porcentaje(resultados[4])}')
    print(f'Partido Morado tiene: {porcentaje(resultados[5])}')
    print(f'Podemos Perú tiene: {porcentaje(resultados[6])}')
    print(f'Renovación Popular tiene: {porcentaje(resultados[7])}')
    print(f'Somos Perú tiene: {porcentaje(resultados[8])}')
    print(f'Victoria Nacional tiene: {porcentaje(resultados[9])}')

def porcentaje(total_partido):
    return "{0:.2f}".format((total_partido[1]/voto_totales)*100)



if __name__ == '__main__':
    
    numero_votantes = int(input("Cuántos van a votar?: "))
    votacion(numero_votantes)


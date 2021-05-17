from random import randint, uniform,random
import random
import sys


class Pista():
    """
    Crea una pista
    """
       
    def __init__(self, num_players):
        self.num_carril = num_players
        self.length = 5000
    	    
    def generarCarriles(self):
        carriles = list(range(num_players))
        #print(carriles)
        carrilesRandom = random.sample(carriles,num_players)
        #print("es random",carrilesRandom)
        for i in range(len(carrilesRandom)):
            carros[i].asignarCarril(carrilesRandom[i]+1)

        

class Player():
    """
    Crea un jugador
    """
    def __init__(self,name = "jugador"):
        self.name = name
        self.carro = 0
    	    
    def asignarCarro(self, carro):
        self.carro=carro
        

class Carro():
    """
    Crea un carro
    """
    def __init__(self,player):
        self.conductor = player
        self.carril = 0
        self.mov_total = 0
        
    def asignarCarril(self,carril):
        self.carril = carril
        print("Se asignó el carril",carril,"al conductor",self.conductor)
        
    def moverse(self):
        mov_mts = (randint(1,6)*100) 
        self.mov_total += mov_mts
        print(self.conductor,"se mueve",mov_mts,"m ","-->","total",self.mov_total,"m")


num_players =0

def juegar():
    # Jugar
    player_name = input("Escribe el nombre de tu jugador \n")

    # Vectores almacenamiento (jugadores, carros, pistas)      
    players = []
    carros= []
    pistas = []
    players.append(Player(player_name))
    carros.append(Carro(players[0].name))

    while True:
        try:    
            num_players = int(input("Selecciona el número de jugadores (entre 3 y 5)\n"))
            if num_players > 5 or  num_players <3 :
                print("selecciona un numero valido")
                continue
            break
        except ValueError:
            print("Sólo puedes ingresar números")
            
    #if isinstance(num_players, (int, float)):
    # Selección de jugadores
    if num_players > 5 :
        num_players = int(input("Por favor selecciona un número válido de jugadores, recuerda que son máximo 5 jugadores \n"))
    else:
        for i in range(1,num_players):
            players.append(Player(i))
            carros.append(Carro(i))
            
    # Creación de pistas
    for i in range(6):
        pistas.append(Pista(num_players))
      
    while True:
        try:    
            pista_sel = int(input("Escoge la pista (puedes escribir un número de 1 a 5 o escribir 0 para seleccionar al azar\n)"))
            if pista_sel > 5 or pista_sel < 0:
                print("Selecciona un número válido")
                continue
                #pista_sel = int(input("Por favor escoge una opción válida: puedes escribir un número de 1 a 5 o escribir 0 para seleccionar al azar\n"))
            elif pista_sel == 0:
                pista_sel = randint(1,5)
                print("Se seleccionó la pista",pista_sel,"de forma aleatoria")
                break
            else:
                print("Se seleccionó la pista",pista_sel)
                break
        except ValueError:
            print("Sólo puedes ingresar números")
       
    print("Y se asignaron los siguientes carriles a los jugadores:")
    pistas[pista_sel].generarCarriles()

    #Inicio de la carrera
    ganadores = []
    j=0
    while j != 3: #or j < num_players:
        distanciaPista = pistas[pista_sel].length;
        for i in range(num_players):
            if carros[i].mov_total >= distanciaPista:
                continue

            carros[i].moverse()

            if carros[i].mov_total >= distanciaPista:
                print("----",players[i].name,"llegó a la meta en la posición",j+1,"----",)
                ganadores.append(players[i].name)
                j += 1
                #if num_players < 3 and j==num_players:
                #   break
                if j==3:
                    break
    volverJugar=input("¿Quieres jugar otra vez?s/n\n")
    return volverJugar
            
"""
Inicio del juego

"""

# Pantalla de inicio
print("*****---- ¡Bienvenido al juego de carreras de Nia! ---- *******")
print("Escoge una opción:\n(Escribe el número de la opción para seleccionarla)")

# Ver histórico(fireBase)
while True:
    try:
        opcionJuego =input("1- Jugar\n2-Ver el histórico de ganadores\n")
        if opcionJuego == "1":
            jugar=0
            while jugar==0:  
                
                keepPlaying=juegar()
                if keepPlaying == "n":
                    jugar=1
        elif opcionJuego == "2":
            break
        else:
            print("Gracias por juegar")
            break
    except ValueError:
        print("Sólo puedes ingresar números")



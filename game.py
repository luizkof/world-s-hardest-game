import pygame, sys
from pygame.locals import *
import numpy as np 
from inimigo import Inimigo
from player import Player
from neural import Neural
# from neural import Neural
import time


#Posicai do fim do jogo
XFINAL = 45
YFINAL = 13



WIDTH = 50
HEIGHT = 50
SIZE_OBJECT = 10
SCREENW = WIDTH*SIZE_OBJECT
SCREENH =  HEIGHT*SIZE_OBJECT
clock = pygame.time.Clock()
enemy = []

#constantes do mapa
LIVRE = 2
PAREDE = 0
INICIO = 1
INIMIGO = 3
INIMIGOV = 4
INIMIGOVV = 5
INIMIGOH = 6
INIMIGOHH = 7
INIMIGOD = 8
INIMIGODD = 9
INIMIGOD1 = 10
INIMIGOD11 = 11
INIMIGOD2 = 12
INIMIGOD22 = 13
PLAYER = 999
#PLAYER
MOV_UP = -1
MOV_DOWN = -2
MOV_LEFT = -3
MOV_RIGHt = -4

#color
WHITE=(255,255,255)
BLUE=(0,0,255)
RED =(255,0,0)
GREEN =(255,0,0)
YELLOW =(255,255,0)
#sensor



def showMap(DISPLAY,matrixMap,players):    
    
    
    count = 0
    for linha , x in zip(matrixMap,range(WIDTH)):
        for elemento, y in zip(linha,range(HEIGHT)):
            if(elemento == INICIO):
                pygame.draw.rect(DISPLAY,GREEN,(x*SIZE_OBJECT,y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
            if(elemento == PAREDE):
                pygame.draw.rect(DISPLAY,BLUE,(x*SIZE_OBJECT,y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
            if(elemento == LIVRE):
                pygame.draw.rect(DISPLAY,WHITE,(x*SIZE_OBJECT,y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
            if(elemento > INIMIGO):
                pygame.draw.rect(DISPLAY,RED,(x*SIZE_OBJECT,y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
    
            # pygame.display.update()
            # if(elemento == 1):
            #     pygame.draw.rect(DISPLAY,RED,(x*SIZE_OBJECT,y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
                
            count = count +1
    
    for p1 in players:
        if(matrixMap[p1.x][p1.y] > INIMIGO):
            p1.vida = 0
            print("morreu")
            
        else:
            if(p1.vida == 0):
                pygame.draw.rect(DISPLAY,(128,128,128),(p1.x*SIZE_OBJECT,p1.y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
            else:
                pygame.draw.rect(DISPLAY,(0,255,0),(p1.x*SIZE_OBJECT,p1.y*SIZE_OBJECT,SIZE_OBJECT,SIZE_OBJECT))
        
        pygame.display.update() 
    return 1
    
def readSensor(DISPLAY,matrixMap,players,sensores):
    count = 0
    for p1,sensor  in zip(players,sensores):
        while(matrixMap[p1.x+count][p1.y] != PAREDE and matrixMap[p1.x+count][p1.y] < INIMIGO and p1.x+count < 50):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), (p1.x*SIZE_OBJECT, p1.y*SIZE_OBJECT), ((p1.x+ count)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['R'] = matrixMap[p1.x+count][p1.y]
        sensor['RCount'] = count
        

        count = 0
        while(matrixMap[p1.x-count][p1.y] != PAREDE and matrixMap[p1.x-count][p1.y] < INIMIGO):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x-count)*SIZE_OBJECT, p1.y*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['L'] = matrixMap[p1.x-count][p1.y]
        sensor['LCount'] = count
        
        
        count = 0
        while(matrixMap[p1.x][p1.y + count] != PAREDE and matrixMap[p1.x][p1.y + count] < INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x)*SIZE_OBJECT, (p1.y+count)*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['U'] = matrixMap[p1.x][p1.y+count]
        sensor['UCount'] = count

        count = 0
        while(matrixMap[p1.x][p1.y - count] != PAREDE and matrixMap[p1.x][p1.y - count] < INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x)*SIZE_OBJECT, (p1.y-count)*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['D'] = matrixMap[p1.x][p1.y - count]
        sensor['DCount'] = count

        count = 0
        while(matrixMap[p1.x - count][p1.y + count] != PAREDE and matrixMap[p1.x-count][p1.y + count] < INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x-count)*SIZE_OBJECT, (p1.y+count)*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['DL'] = matrixMap[p1.x-count][p1.y + count]
        sensor['DLCount'] = count

        count = 0
        while(matrixMap[p1.x + count][p1.y + count] != PAREDE and matrixMap[p1.x+count][p1.y + count] < INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x+count)*SIZE_OBJECT, (p1.y+count)*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['DR'] = matrixMap[p1.x+count][p1.y + count]
        sensor['DRCount'] = count
        
        count = 0
        while(matrixMap[p1.x + count][p1.y - count] != PAREDE and matrixMap[p1.x+count][p1.y - count] < INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x + count)*SIZE_OBJECT, (p1.y-count)*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['UR'] = matrixMap[p1.x+count][p1.y - count]
        sensor['URCount'] = count

        count = 0
        while(matrixMap[p1.x - count][p1.y - count] != PAREDE and matrixMap[p1.x-count][p1.y - count] < INIMIGO ):
            count +=1
        pygame.draw.line(DISPLAY, (0,150,0), ((p1.x - count)*SIZE_OBJECT, (p1.y-count)*SIZE_OBJECT), ((p1.x)*SIZE_OBJECT, p1.y*SIZE_OBJECT))
        sensor['UL'] = matrixMap[p1.x-count][p1.y - count]
        sensor['ULCount'] = count

    # print(sensor)
    


def criaInimigos():
    enemy.append(Inimigo('v',16,25,10))
    enemy.append(Inimigo('v',18,25,10))
    enemy.append(Inimigo('v',20,25,10))
    enemy.append(Inimigo('v',22,25,10))
    enemy.append(Inimigo('v',24,25,10))
    enemy.append(Inimigo('v',26,25,10))
    enemy.append(Inimigo('v',28,25,10))
    enemy.append(Inimigo('v',30,25,10))
    enemy.append(Inimigo('v',30,25,10))


    # enemy.append(Inimigo('h',25,16,10))
    # enemy.append(Inimigo('h',25,18,10))
    # enemy.append(Inimigo('h',25,20,10))
    # enemy.append(Inimigo('h',25,22,10))
    # enemy.append(Inimigo('h',25,24,10))
    # enemy.append(Inimigo('h',25,26,10))
    # enemy.append(Inimigo('h',25,28,10))
    # enemy.append(Inimigo('h',25,30,10))
    # enemy.append(Inimigo('h',25,30,10))

    # enemy.append(Inimigo('d1',25,16,10))
    # enemy.append(Inimigo('d1',25,18,10))
    # enemy.append(Inimigo('d1',25,20,10))
    # enemy.append(Inimigo('d1',25,22,10))
    # enemy.append(Inimigo('d1',25,24,10))
    # enemy.append(Inimigo('d1',25,26,10))
    # enemy.append(Inimigo('d1',25,28,10))
    # enemy.append(Inimigo('d1',25,30,10))
    # enemy.append(Inimigo('d1',25,30,10))


    
    
    # enemy.append(Inimigo('d2',25,18,10))
    # enemy.append(Inimigo('d2',25,20,10))
    # enemy.append(Inimigo('d2',25,22,10))
    # enemy.append(Inimigo('d2',25,24,10))
    # enemy.append(Inimigo('d2',25,26,10))
    # enemy.append(Inimigo('d2',25,28,10))
    # enemy.append(Inimigo('d2',25,30,10))
    # enemy.append(Inimigo('d2',25,30,10))
    
    
    # enemy.append(Inimigo('v',22,30,50))
    # enemy.append(Inimigo('h',10,30,10))
def criaMapa(WIDTH,HEIGHT):
    mapa = np.loadtxt(open("mapa.csv", "rb"), delimiter=",", skiprows=1)
    mapa = np.transpose(mapa)
    print(mapa.shape)
    
    
    
    

    return mapa
def movimentaPlayer(p1,mapa,movimento):
    if movimento == 276 or movimento == 0:
        if(not(p1.step(mapa,MOV_LEFT))):
            print("GAME OVER")
            p1.vida = 0
    if movimento == 275 or movimento == 1:
        if(not(p1.step(mapa,MOV_RIGHt))):
            print("GAME OVER")
            p1.vida = 0            
    if movimento == 273 or movimento == 2:
        if(not(p1.step(mapa,MOV_UP))):
            print("GAME OVER")
            p1.vida = 0
    if movimento == 274 or movimento == 3:
        if(not(p1.step(mapa,MOV_DOWN))):
            print("GAME OVER")
            p1.vida = 0

################################################################################################################################################################################

# Algoritmo Genetico



def fitness(players,p1_redes,sensores):
    mainGame(players,p1_redes,sensores,True)
    
def mutacao():
    pass

def main():
    players = []
    p1_redes = []


    sensor = {
        'U':0,
        'UCount':0,
        'L':0,
        'LCount':0,
        'R':0,
        'RCount':0,
        'D':0,
        'DCount':0,
        'UR':0,
        'URCount':0,
        'DR':0,
        'DRCount':0,
        'DL':0,
        'DLCount':0,
        'UL':0,
        'ULCount':0

    }
    sensores = []
    
    #caso queira jogar só
    while(0):
        players.append(Player(1,12))
        p1_redes.append(Neural(len(sensor.values()),np.array([5,3,4])))
        sensores.append(sensor)

        mainGame(players,p1_redes,sensores,False)

    NUM_POP = 100
    
    # Inicializa pop
    for _ in range(NUM_POP):
        players.append(Player(1,12))
        p1_redes.append(Neural(len(sensor.values()),np.array([5,3,4])))
        sensores.append(sensor)

        
    
    #Inicio de uma geração
    fitness(players,p1_redes,sensores)
    

    
    #fim de uma geração






################################################################################################################################################################################

def mainGame(players,p1_redes,sensores,isMaquina):
    
    pygame.init()
    DISPLAY = pygame.display.set_mode((SCREENW,SCREENH))
    pygame.display.set_caption('O jogo mais dificl do mundo')
    global enemy
    enemy = []
    criaInimigos()
    # mapa
    mapa = criaMapa(WIDTH,HEIGHT)
    
    ####
    
    
    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)

    #condigura player
    # p1.setMap(mapa)
    
    
    

    count = 0
    fimJogo = False
    while not(fimJogo):
        #Vez do player
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); #sys.exit() if sys is imported
            if event.type == pygame.KEYDOWN:
                # print(event.key)
                # pause = p
                if event.key == 112:                    
                    print(p1.__dict__)
                if event.key == 115:                    
                    print(sensor)
                if(movimentaPlayer(players[0],mapa,event.key) == 0): 
                    fimJogo = True
                
                
                

        # Vez do inimigo                    
        for a in enemy:
            a.step(mapa)
        # Vez da Maquina
        readSensor(DISPLAY, mapa,players,sensores)# já configura os sensoress
        if(isMaquina):
            for p1,p1_rede,sensor in zip(players,p1_redes,sensores):
                print("a")
                if(p1.vida == 1):
                    # print("movimenta")
                    movimento = p1_rede.predict(np.array(list(sensor.values())))
                    movimentaPlayer(p1,mapa,movimento)
                    
        fimJogo = True
        for p1 in players:
            if(p1.vida == 1): 
                fimJogo = False

        showMap(DISPLAY,mapa,players) 
            
        # distancia =pow(pow(p1.x - XFINAL,2) + pow(p1.y - YFINAL,2),0.5)
        # print(distancia)
        
        clock.tick(1000000)
    # retorna o fitness
    
    distancia =pow(pow(p1.x - XFINAL,2) + pow(p1.y - YFINAL,2),0.5)
    print(distancia)
    return distancia
    

main()
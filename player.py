import numpy as np
class Player:
    #constantes do mapa
    LIVRE = 2
    PAREDE = 0
    INICIO = 1
    INIMIGO = 3
    PLAYER = 999

    MOV_UP = -1
    MOV_DOWN = -2
    MOV_LEFT = -3
    MOV_RIGHt = -4
    def __init__(self,mapa,x,y):
        self.mapaPlayer = np.zeros((len(mapa),len(mapa)))
        self.x = x
        self.y = y
        mapa[x][y] = self.PLAYER
        
        
    def step(self,mapa,movimento):
        
        if(self.x < 4 or self.x > 44) :
            mapa[self.x][self.y] = self.INICIO
        else: 
            mapa[self.x][self.y] = self.LIVRE


        if(movimento == self.MOV_DOWN):
            if(mapa[self.x][self.y+1] == self.PAREDE):
                self.mapaPlayer[self.x][self.y] = 1
                return False
            else:
                self.y += 1
                self.mapaPlayer[self.x][self.y] = 1
                
        if(movimento == self.MOV_RIGHt):
            if(mapa[self.x +1 ][self.y] == self.PAREDE):
                self.mapaPlayer[self.x][self.y] = 1
                return False
            else:
                if(self.x != len(mapa[0])):
                    self.x += 1
                    print(self.x)
                self.mapaPlayer[self.x][self.y] = 1
        if(movimento == self.MOV_UP):
            if(mapa[self.x][self.y-1] == self.PAREDE ):
                self.mapaPlayer[self.x][self.y] = 1
                return False
            else:
                self.y -= 1
                self.mapaPlayer[self.x][self.y] = 1
        if(movimento == self.MOV_LEFT):
            if(mapa[self.x -1 ][self.y] == self.PAREDE):
                self.mapaPlayer[self.x][self.y] = 1
                return False
            else:
                if(self.x != 0):
                    self.x -= 1
                self.mapaPlayer[self.x][self.y] = 1
        return True
    
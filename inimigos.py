import pygame
from constantes import *


#-------------------------------------------------------------------Spitter--------------------------------------------------------     
class Tiro(pygame.sprite.Sprite):
    def __init__(self,posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Slimes/Spitter/SpitterShoot.png')
        self.rect = self.image.get_rect()
        
        self.velocidade = 5 #aumentando a variavel de velocidade modificamos a frequencia de balas
        self.rect.top = posy
        self.rect.left = posx
        self.direcao = -1

    def movimento(self):
        self.rect.left += self.velocidade*self.direcao

    def direcao(self,pos_player, pos_mob):
        if pos_player <= pos_mob:
            direcao = -1
        elif pos_player >= pos_mob:
            direcao = 1

        
class SlimeSpitter (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.posAnim = 0
        self.image = SlimeSpritterWalk[self.posAnim]
        self.rect = self.image.get_rect()

        self.levelShift = 0
        self.vida = True
        self.animStart = 0
        self.xIni = x
        self.yIni = y
        self.rect.x = x
        self.rect.y = y
        self.listDisparo = pygame.sprite.Group()

    def morrer():
        self.kill
        
    def colocar(self, superficie):
        superficie.blit(self.image, self.rect)

    def disparar(self):
        minhabala = Tiro(self.rect.left-10,self.rect.centery)
        self.listDisparo.add(minhabala)

    def morrer(self):
        self.vida = False
        self.animStart = pygame.time.get_ticks()

    def movimento(self):
        self.rect.x = self.xIni+self.levelShift
        return


        
#--------------------------------------------------------------------------GENERAL---------------------------------------------------------------------
class SlimeGeneral(pygame.sprite.Sprite):
    def __init__(self, x, y, xmin, xmax):
        super().__init__()
        
        self.image = pygame.Surface([64,64], pygame.SRCALPHA)
        self.image.blit(SlimeGeneralWalk[0],(0,0))
        
        self.rect = self.image.get_rect()

        self.animStart = 0
        self.vida = True
        self.vel = 1.2
        self.direcao = 1
        self.posIni = [x,y]
        self.posAtual = [x,y]
        self.mMx = [xmin,xmax]
        self.levelShift = 0

    def __direcao(self,lim_min,lim_max):
        if self.rect.left <= lim_min:
            self.direcao = 1
        elif self.rect.right >= lim_max:
            self.direcao = -1
            
    def movimento(self):
        if self.vida:
            animPos = ((pygame.time.get_ticks()-self.animStart)//150)
            if(self.animStart == 0  or animPos >= len(SlimeGeneralWalk)):
                self.animStart = pygame.time.get_ticks()
                animPos = ((pygame.time.get_ticks()-self.animStart)//150)

            
            self.image.fill((255,255,255,0))
            self.image.blit(SlimeGeneralWalk[animPos],(0,0))
            if self.direcao == 1:
                flipped = pygame.transform.flip(self.image,True,False)
                self.image = flipped
                
            self.posAtual[0] += (self.vel*self.direcao)
        self.__direcao(self.mMx[0]+self.levelShift,self.mMx[1]+self.levelShift)    
        self.rect.x = self.posAtual[0]+self.levelShift

    def morrer(self):
        posAnim = (pygame.time.get_ticks()-self.animStart)//150
        self.image.fill((255,255,255,0))
            
        if(posAnim >= len(SlimeGeneralDeath)):
            self.kill()
        else:
            self.image.blit(SlimeGeneralDeath[posAnim],(0,0))   

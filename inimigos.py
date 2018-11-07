import pygame
from constantes import *


class SlimeGeneral(pygame.sprite.Sprite):
    def __init__(self, x, y, xmin, xmax):
        super().__init__()
        
        self.image = pygame.Surface([64,64], pygame.SRCALPHA)
        self.image.blit(SlimeGeneralWalk[0],(0,0))
        
        self.rect = self.image.get_rect()

        self.animStart = 0
        self.vida = True
        self.vel = 1.2
        self.direcao = True
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
        if self.vida == True:
            print("A")
            if(self.animStart == 0):
                self.animStart = pygame.time.get_ticks()
            self.__direcao(self.mMx[0]+self.levelShift,self.mMx[1]+self.levelShift)
            self.posAtual[0] += (self.vel*self.direcao)
            self.rect.x = self.posAtual[0]+self.levelShift

    def morrer(self):
        posAnim = (pygame.time.get_ticks()-self.animStart)//150
        self.image.fill((255,255,255,0))
            
        if(posAnim >= len(SlimeGeneralDeath)):
            self.kill()
        else:
            self.image.blit(SlimeGeneralDeath[posAnim],(0,0))   

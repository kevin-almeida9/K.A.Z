import pygame
from constantes import *


#-------------------------------------------------------------------Spitter--------------------------------------------------------     
class Tiro(pygame.sprite.Sprite):
    def __init__(self,posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Slimes/Spitter/SpitterShoot.png')
        self.rect = self.image.get_rect()
        
        self.velocidade = 5 #aumentando a variavel de velocidade modificamos a frequencia de balas
        self.rect.y = posy
        self.rect.x = posx
        self.direcao = -1

    def movimento(self):
        self.rect.x += self.velocidade*self.direcao

    def direcao(self,pos_player, pos_mob):
        if pos_player <= pos_mob:
            direcao = -1
        elif pos_player >= pos_mob:
            direcao = 1

        
class SlimeSpitter (pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([64,64], pygame.SRCALPHA)
        self.rect = self.image.get_rect()

        self.levelShift = 0
        self.invulneravel = 0
        self.vida = 1
        self.vivo = True
        self.animStart = 0
        self.atirou = False
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
        animPos = (pygame.time.get_ticks() - self.animStart)//150
        if(animPos >= len(SlimeSpitterShoot)):
            self.atirou = False
            self.animStart = pygame.time.get_ticks()
            animPos = (pygame.time.get_ticks() - self.animStart)//150
        if(animPos == 5):
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
        self.invulneravel = 0
        self.vida = 1
        self.vivo = True
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
            
#--------------------------------------------------------------------------HELI SLIME---------------------------------------------------------------------
class HeliSlime (pygame.sprite.Sprite):
    def __init__(self, x, y, pos_min, pos_max, sentido):
        super().__init__()
        self.image = pygame.Surface([64,64], pygame.SRCALPHA)
        self.image.blit(HeliSlimeFly[0],(0,0))
        
        self.rect = self.image.get_rect()

        self.sentido = sentido       
        self.animStart = 0
        self.invulneravel = 0
        self.vida = 1
        self.vivo = True
        self.vel = 1.2
        self.direcao = 1
        self.posIni = [x,y]
        self.posAtual = [x,y]
        self.mMpos = [pos_min,pos_max]
        self.levelShift = 0

        def __direcao(self,lim_min,lim_max):
            if self.rect.left <= lim_min:
                self.direcao = 1
            elif self.rect.right >= lim_max:
                self.direcao = -1

        
    def __direcao(self,lim_min,lim_max):

        if self.sentido == 'x':
            if self.rect.left <= lim_min:
                self.direcao = 1
            elif self.rect.right >= lim_max:
                self.direcao = -1
        elif self.sentido == 'y':
            if self.rect.top <= lim_min:
                self.direcao = 1
            elif self.rect.bottom >= lim_max:
                self.direcao = -1
            
    def movimento(self):
        if self.sentido == 'x':
            if self.vida:
                animPos = ((pygame.time.get_ticks()-self.animStart)//150)
                if(self.animStart == 0  or animPos >= len(HeliSlimeFly)):
                    self.animStart = pygame.time.get_ticks()
                    animPos = ((pygame.time.get_ticks()-self.animStart)//150)

                
                self.image.fill((255,255,255,0))
                self.image.blit(HeliSlimeFly[animPos],(0,0))
                if self.direcao == 1:
                    flipped = pygame.transform.flip(self.image,True,False)
                    self.image = flipped
                    
                self.posAtual[0] += (self.vel*self.direcao)
            self.__direcao(self.mMpos[0]+self.levelShift,self.mMpos[1]+self.levelShift)    
            self.rect.x = self.posAtual[0]+self.levelShift

            
        elif self.sentido == 'y':
            if self.vida:
                animPos = ((pygame.time.get_ticks()-self.animStart)//150)
                if(self.animStart == 0  or animPos >= len(HeliSlimeFly)):
                    self.animStart = pygame.time.get_ticks()
                    animPos = ((pygame.time.get_ticks()-self.animStart)//150)

                
                self.image.fill((255,255,255,0))
                self.image.blit(HeliSlimeFly[animPos],(0,0))
                
                    
                self.posAtual[1] += (self.vel*self.direcao)
            self.__direcao(self.mMpos[0]+self.levelShift,self.mMpos[1]+self.levelShift)    
            self.rect.y = self.posAtual[1]+self.levelShift

   
    def morrer(self):
        """posAnim = (pygame.time.get_ticks()-self.animStart)//150
        self.image.fill((255,255,255,0))
            
        if(posAnim >= len(SlimeGeneralDeath)):
            self.kill()
        else:
            self.image.blit(SlimeGeneralDeath[posAnim],(0,0))"""
        self.kill()
               

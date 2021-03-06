import pygame
from constantes import *
import inimigos


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height, imagem):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.image.blit(imagem,(0,0))
 
        self.rect = self.image.get_rect()

class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.spawnPointx = 0
        self.spawnPointy = 0
        self.player = player
        self.shift = 0;
        self.max = 0;
         
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        for enemy in self.enemy_list:
            if enemy.invulneravel > 0:
                b = pygame.time.get_ticks() - enemy.invulneravel
                if(b>1000):  
                    enemy.invulneravel = 0
            if not enemy.vivo:
                enemy.levelShift = self.shift
                enemy.morrer()
 
    def draw(self, screen):
        """ Draw everything on this level. """
        # Draw the background
        screen.blit(self.background,(self.shift,0))
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        

    def enemyMove(self):
         for s in self.enemy_list:
            s.levelShift = self.shift
            s.movimento()

class LevelFinal(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform
        level = [[832,192,0,412,pygame.image.load('Plataformas\Plataforma1.png')],
                 [248,448,914,156,pygame.image.load('Plataformas\Plataforma3.png')],
                 [188,320,764,284,pygame.image.load('Plataformas\Plataforma2.png')],
                 [188,320,1130,284,pygame.image.load('Plataformas\Plataforma4.png')],
                 [384,192,1236,412,pygame.image.load('Plataformas\Plataforma5.png')],
                 [128,192,1720,412,pygame.image.load('Plataformas\Plataforma6.png')],
                 [256,192,2098,412,pygame.image.load('Plataformas\Plataforma7.png')],
                 [128,192,2454,412,pygame.image.load('Plataformas\Plataforma8.png')],
                 [128,192,2682,412,pygame.image.load('Plataformas\Plataforma9.png')],
                 [192,256,3074,344,pygame.image.load('Plataformas\Plataforma11.png')],
                 [192,192,2950,408,pygame.image.load('Plataformas\Plataforma10.png')],
                 [448,12,3262,348,pygame.image.load('Plataformas\Plataforma12.png')],
                 [256,256,3706,344,pygame.image.load('Plataformas\Plataforma13.png')],
                 [896,192,3924,412,pygame.image.load('Plataformas\Plataforma14.png')]]

        # Array x , y do inimigo
        slimeGeneralList = [[564,371,337,769],
                            [1403,371,1245,1559],
                            [2201,371,2107,2297],
                            [3020,367,2957,3090],
                            [3098,303,3098,3906],
                            [3906,303,3098,3906],
                            [4145,371,3924,4359],
                            [4585,371,4366,4759]
                            ]

        slimeSpitterList = [[564,371]]
        
        HeliSlimeList = [[564,371,30,375,"y"],
                         [350,40,30,375,"y"]]
        
        # Inicia Variaveis
        self.spawnPointx = 150
        self.spawnPointy = 412
        player.rect.x = self.spawnPointx
        player.rect.bottom = self.spawnPointy
        self.background = pygame.image.load("Background\Background.png")
        # Go through the array above and add platforms
        for platform in level:
            if(self.max < platform[0]+platform[2]-50):
                self.max = platform[0]+platform[2]-50
            block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.top = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for sg in slimeGeneralList:
            enemy = inimigos.SlimeGeneral(sg[0],sg[1],sg[2],sg[3])
            enemy.rect.x = sg[0]
            enemy.rect.y = sg[1]-22
            self.enemy_list.add(enemy)

        for sp in slimeSpitterList:
            enemy = inimigos.SlimeSpitter(sp[0],sp[1]-22)
            self.enemy_list.add(enemy)

        for sh in HeliSlimeList:
            enemy = inimigos.HeliSlime(sh[0],sh[1],sh[2],sh[3],sh[4])
            enemy.rect.x = sh[0]
            enemy.rect.y = sh[1]-22
            self.enemy_list.add(enemy)
            
            
class LevelP3(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform
        level = [[576,192,0,1008,pygame.image.load('Plataformas\PlataformasP3\Plataforma1.png')],
                 [1024,448,1344,752,pygame.image.load('Plataformas\PlataformasP3\Plataforma2.png')],
                 [768,320,1600,880,pygame.image.load('Plataformas\PlataformasP3\Plataforma3.png')],
                 [576,192,1408,1008,pygame.image.load('Plataformas\PlataformasP3\Plataforma4.png')],
                 [384,128,2477,1072,pygame.image.load('Plataformas\PlataformasP3\Plataforma5.png')],
                 [512,256,2688,944,pygame.image.load('Plataformas\PlataformasP3\Plataforma6.png')],
                 [128,128,3072,816,pygame.image.load('Plataformas\PlataformasP3\Plataforma7.png')],
                 [320,256,2880,688,pygame.image.load('Plataformas\PlataformasP3\Plataforma8.png')],
                 [832,826,2368,374,pygame.image.load('Plataformas\PlataformasP3\Plataforma9.png')],
                 [3200,1216,0,-16,pygame.image.load('Plataformas\PlataformasP3\Plataforma10.png')],
                 [256,324,2432,374,pygame.image.load('Plataformas\PlataformasP3\Escada.png')]]

        # Array x , y do inimigo
        slimeGeneralList = []

        slimeSpitterList = []
        
        HeliSlimeList = []
        
        # Inicia Variaveis
        self.spawnPointx = 150
        self.spawnPointy = 412
        player.rect.x = self.spawnPointx
        player.rect.bottom = self.spawnPointy
        self.background = pygame.image.load("Background\Background.png")
        # Go through the array above and add platforms
        for platform in level:
            if(self.max < platform[0]+platform[2]-50):
                self.max = platform[0]+platform[2]-50
            block = Platform(platform[0], platform[1], platform[4])
            block.rect.x = platform[2]
            block.rect.top = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for sg in slimeGeneralList:
            enemy = inimigos.SlimeGeneral(sg[0],sg[1],sg[2],sg[3])
            enemy.rect.x = sg[0]
            enemy.rect.y = sg[1]-22
            self.enemy_list.add(enemy)

        for sp in slimeSpitterList:
            enemy = inimigos.SlimeSpitter(sp[0],sp[1]-22)
            self.enemy_list.add(enemy)

        for sh in HeliSlimeList:
            enemy = inimigos.HeliSlime(sh[0],sh[1],sh[2],sh[3],sh[4])
            enemy.rect.x = sh[0]
            enemy.rect.y = sh[1]-22
            self.enemy_list.add(enemy)
            

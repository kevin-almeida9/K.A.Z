from constantes import *
import pygame
import fases
import inimigos

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
        self.levelShift = 0
        self.vel = 5

        self.animDelay = 1
        self.animAnt = 0
        self.animStart = 0
        self.animCount = 0
        self.anim = [KAZIdleAnim]

        self.direcao = False
        self.atacando = False
        self.invulneravel = 0
        
        self.vida = 3
        # Call the parent's constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.width = 56
        self.height = 98
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        self.image.blit(KAZIdleAnim,(0,0))
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            if self.change_y < 10:
                self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= ScreenHeight - self.rect.height-10 and self.change_y >= 0:
            self.vida = 0
            self.rect.bottom = ScreenHeight
            self.change_y = 0
            
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for block in block_hit_list:
            '''if(type(block) != type(fases.Platform(0,0,pygame.Surface([0,0])))):
                # If we are moving right,
                # set our right side to the left side of the item we hit
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                elif self.change_x < 0:
                    # Otherwise if we are moving left, do the opposite.
                    self.rect.left = block.rect.right'''
            if(type(block) == type(inimigos.SlimeGeneral(0,0,0,0)) or type(block) == type(inimigos.HeliSlime(0,0,0,0,0))):
                if(self.atacando and block.vivo == True and block.invulneravel == 0):
                    block.vida -= 1
                    block.invulneravel = pygame.time.get_ticks()
                    if(block.vida <= 0):
                        block.vivo = False
                        block.animStart = pygame.time.get_ticks()
                elif(self.invulneravel == 0 and block.vida):
                    self.vida-=1
                    self.invulneravel = pygame.time.get_ticks()
                        
                
                    
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if(type(block) == type(fases.Platform(0,0,pygame.Surface([0,0])))):
                if self.rect.bottom < block.rect.top+11:
                    self.rect.bottom = block.rect.top
                    if self.change_y > 0:
                        self.change_y = 0
 
            # Stop our vertical movement
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= ScreenHeight:
            if(self.rect.bottom >= ScreenHeight):
                self.change_y = -10
            if len(platform_hit_list) > 0:
                for objeto in platform_hit_list:
                    if type(objeto) == type(fases.Platform(0,0,pygame.Surface([0,0]))):
                        if(self.rect.bottom < objeto.rect.top+10):
                            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.animator(2)
        self.direcao = True
        self.change_x = -self.vel
        
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.animator(2)
        self.direcao = False
        self.change_x = self.vel
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.animator(3)
        self.change_x = 0


    def death(self, animPosition):
        self.image.fill((255,255,255,0))
        self.image.blit(KAZDeath[animPosition],(0,0))
        #INVERTE CASO DIREÇÃO SEJA TRUE
        if(self.direcao):
            flipped = pygame.transform.flip(self.image,True,False)
            self.image = flipped
        
    def attack(self,animPosition):
        self.image.fill((255,255,255,0))
        self.image.blit(KAZAttack[animPosition],(0,0))
        #INVERTE CASO DIREÇÃO SEJA TRUE
        if(self.direcao):
            flipped = pygame.transform.flip(self.image,True,False)
            self.image = flipped

    def animator(self, atual = None):
        '''
        0 - Ataque
        1 - Pulo
        2 - Andando
        3 - Idle
        '''
        
        if atual != self.animAnt and atual != None:
            self.animStart = pygame.time.get_ticks()
            self.animAnt = atual

            if atual == 0:
                self.image = pygame.Surface([96, 96], pygame.SRCALPHA)
                self.anim = KAZAttack
                self.animDelay = 80
            #elif atual == 1:
                #anim = KAZJump
            elif atual == 2:
                self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
                self.anim = KAZRunning
                self.animDelay = 150
            elif atual == 3:
                self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
                self.animDelay = 1
                self.anim = [KAZIdleAnim]
                self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
                self.image.blit(KAZIdleAnim,(0,0))

        else:
            self.image.fill((255,255,255,0))
            self.animCount = (pygame.time.get_ticks()-self.animStart)//self.animDelay 
            
            if(self.animAnt == 3):
                self.image.blit(KAZIdleAnim,(0,0))
            elif(self.animCount >= len(self.anim)):
                if(self.animAnt == 0):
                    self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
                    self.atacando = False
                    self.animStart = 0
                    self.animator(3)
                    if(self.direcao):
                        self.rect.x += 44
                else:
                    self.animStart = pygame.time.get_ticks()
                    self.animCount = (pygame.time.get_ticks()-self.animStart)//self.animDelay
            else:
                self.image.blit(self.anim[self.animCount],(0,0))
            
            if(self.direcao):
                flipped = pygame.transform.flip(self.image,True,False)
                self.image = flipped
        
            

                
def update(spriteList):
    spriteList.update()


def main():
    """ Main Program """
    pygame.init()
    
    # Set the height and width of the screen
    size = [ScreenWidth, ScreenHeight]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("K.A.Z.")
 
    # Create the player
    player = Player()
    
    # Create all the levels
    level_list = []
    '''level_list.append(fases.LevelFinal(player))'''
    level_list.append(fases.LevelP3(player))
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done:
        player.animator()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if(player.atacando == False):
                    if event.key == pygame.K_LEFT:
                        player.go_left()
                    if event.key == pygame.K_RIGHT:
                        player.go_right()
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        player.jump()
                    if event.key == pygame.K_c:
                        player.stop()
                        player.atacando = True
                        player.animator(0)
                        if(player.direcao):
                            player.rect.x -= 44
                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
 
        # Update the player.
        if(player.vida <= 0):
            a = True
            player.stop()
            player.animStart = pygame.time.get_ticks()
            player.image = pygame.Surface([96,96],pygame.SRCALPHA)
            while a:
                animPosition = (pygame.time.get_ticks()- player.animStart)//250
                if(animPosition >= len(KAZDeath)):
                    player.kill()
                    a = False
                else:
                    player.death(animPosition)
                    current_level.draw(screen)
                    active_sprite_list.draw(screen)
                    active_sprite_list.update()
                    pygame.display.flip()
            main()
                
        #Tempo de invulnerabilidade    
        if(player.invulneravel > 0):
            b = pygame.time.get_ticks() - player.invulneravel
            if(b >= 2500): #2500ms
                player.invulneravel = 0

        
        
        update(active_sprite_list)
 
        # Update items in the level
        update(current_level)

        
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right > ScreenWidth-200:

            if player.levelShift+ScreenWidth-player.vel <= player.level.max:
                player.rect.right = ScreenWidth-200
                player.levelShift+=player.vel
                player.level.shift = -player.levelShift
                player.level.enemyMove()
                for platform in player.level.platform_list:
                    platform.rect.x-=player.vel
            elif player.rect.right >= ScreenWidth:
                player.rect.right = ScreenWidth
 
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left < 200:
            if player.levelShift-player.vel+200 >= 200:
                player.rect.left = 200
                player.levelShift-=player.vel
                player.level.shift = -player.levelShift
                player.level.enemyMove()
                for platform in player.level.platform_list:
                    platform.rect.x+=player.vel
            elif player.rect.left <= 0:
                player.rect.left = 0

                
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        current_level.draw(screen)
        active_sprite_list.draw(screen)
        player.level.enemyMove()
        for i in range(player.vida):
            screen.blit(KAZLifeIcon,(i*35,0))
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        if(player.rect.x+player.levelShift >= player.level.max-100):
            player.vida = 0
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
 
if __name__ == "__main__":
    main()

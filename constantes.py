import pygame

ScreenWidth = 800
ScreenHeight = 600

btnRectSize = [180, 45]

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
DarkGreen = (17,95,0)
Blue = (0,0,255)

def stamina(qual):
    if(qual):
        Stamina = (102,104,255)
    else:
        Stamina = (117,59,144)
    return Stamina

#---------------------------------------------------------------TELAS-----
GameOverBG = pygame.image.load('BackGround\GameOver.png')
MenuBG = pygame.image.load('BackGround\MenuTemp.png')

#--------------------------------------------------------------------Animações-------------------------------------------------------------------
#K.A.Z
#CORRENDO
KAZRunning =[pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim0.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim1.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim2.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim3.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim4.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim5.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim6.png'),
             pygame.image.load('KAZ\RunningAnimation\KAZRunRAnim7.png')]

#IDLE
KAZIdleAnim = pygame.image.load('KAZ\RunningAnimation\KAZRIdle.png')

#DASH
KAZDashing = [pygame.image.load('KAZ\DashingAnimation\KAZRightDash0.png'),
              pygame.image.load('KAZ\DashingAnimation\KAZRightDash1.png'),
              pygame.image.load('KAZ\DashingAnimation\KAZRightDash2.png')]

#ATTACK
KAZAttack = [pygame.image.load('KAZ\AttackAnimation\KAZRightAttack0.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack1.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack2.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack3.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack4.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack5.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack6.png'),
             pygame.image.load('KAZ\AttackAnimation\KAZRightAttack7.png')]

#DEATH
KAZDeath = [pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation0.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation1.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation2.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation3.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation4.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation5.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation6.png'),
            pygame.image.load('KAZ\DeathAnimation\KAZDeathAnimation7.png'),]


#SLIME GENERAL
#ANDANDO
SlimeGeneralWalk = [pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral0.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral1.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral2.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral3.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral4.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral5.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral6.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralWalking\SlimeGeneral7.png')]

#MORRENDO
SlimeGeneralDeath = [pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath0.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath1.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath2.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath3.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath4.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath5.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath6.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath\SlimeGeneralDeath7.png')]

#SLIME Spitter
#ANDANDO
SlimeSpitterWalk = [pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation0.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation1.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation2.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation3.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation4.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation5.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation6.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeWalking/SpitterWalkLAnimation7.png')]

#MORRENDO
SlimeSpitterDead = [pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation0.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation1.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation2.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation3.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation4.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation5.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation6.png'),
                     pygame.image.load('Slimes/SpitterSlime/SpitterSlimeDeath/SpitterDeathAnimation7.png')]

#ATIRANDO
SlimeSpitterShoot = [pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation0.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation1.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation2.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation3.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation4.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation5.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation6.png'),
                      pygame.image.load('Slimes/SpitterSlime/SpitterSlimeAttackAnimation/SpitterAttackAnimation7.png')]

#Heli Slime
#VOANDO
HeliSlime = [pygame.image.load('Slimes/HeliSlime/HeliWalkingAnimation0.png'),
             pygame.image.load('Slimes/HeliSlime/HeliWalkingAnimation1.png'),
             pygame.image.load('Slimes/HeliSlime/HeliWalkingAnimation2.png'),
             pygame.image.load('Slimes/HeliSlime/HeliWalkingAnimation3.png'),
             pygame.image.load('Slimes/HeliSlime/HeliWalkingAnimation4.png'),
             pygame.image.load('Slimes/HeliSlime/HeliWalkingAnimation5.png')]
             
#-----------------------------------------------------------------------ICONES-------------------------------------------------------------------------
KAZLifeIcon = pygame.image.load('KAZ\Life\LifeIconIcon.png')
SpitterShoot = pygame.image.load('Slimes\SpitterSlime\SpitterShoot.png')
selectedOption = pygame.image.load('Background\SelectedOption.png')

#-------------------------------------------------------------------cenario--------------------------------------------------------------------

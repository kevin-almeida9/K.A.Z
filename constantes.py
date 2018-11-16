import pygame

ScreenWidth = 800
ScreenHeight = 600

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

def stamina(qual):
    if(qual):
        Stamina = (102,104,255)
    else:
        Stamina = (117,59,144)
    return Stamina

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
SlimeGeneralWalk = [pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral0.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral1.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral2.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral3.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral4.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral5.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral6.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneral7.png')]

#MORRENDO
SlimeGeneralDeath = [pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath0.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath1.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath2.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath3.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath4.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath5.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath6.png'),
                    pygame.image.load('Slimes\SlimeGeneral\SlimeGeneralDeath7.png')]

#SLIME Spitter
#ANDANDO
SlimeSpitterWalk = [pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation0.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation1.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation2.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation3.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation4.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation5.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation6.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlime/SpitterWalkLAnimation7.png')]

#MORRENDO
SlimeSpitterDead = [pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation0.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation1.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation2.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation3.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation4.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation5.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation6.png'),
                     pygame.image.load('Slimes/Spitter/SpitterSlimeDeath/SpitterDeathAnimation7.png')]

#ATIRANDO
SlimeSpitterShoot = [pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation0.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation1.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation2.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation3.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation4.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation5.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation6.png'),
                      pygame.image.load('Slimes/Spitter/SpitterSlimeAttackAnimation/SpitterAttackAnimation7.png')]
#-----------------------------------------------------------------------ICONES-------------------------------------------------------------------------
KAZLifeIcon = pygame.image.load('KAZ\Life\LifeIconIcon.png')


#-------------------------------------------------------------------cenario--------------------------------------------------------------------
